import datetime

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.contrib import messages
from django.contrib.auth import get_user_model

from cdspec.models import SpecRun
from .forms import CreateForm, EditForm
from cdspec.util import handle_file_upload, Units, graph_format
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from django.db.models import Q

# Create your views here.

#Index View, a list of last ten objects
class IndexView(generic.ListView):
    template_name = "cdspec/index.html"
    context_object_name = 'latest_runs'

    def get(self, request, *args, **kwargs):
        # Get the queryset first
        queryset = self.get_queryset()
        
        # Prepare context
        context = {
            'latest_runs': queryset
        }
        
        # Add username if provided in kwargs
        if kwargs:
            context['username'] = kwargs['user']
            
        return render(request, 'cdspec/index.html', context)

    def get_queryset(self):
        #if uploadedby=user argument is passed, filter the table
        if self.kwargs:
           user = get_user_model().objects.get(username=self.kwargs['user'])
           return SpecRun.objects.filter(upload_user=user).order_by('-upload_date')[:10]
        else:
           return SpecRun.objects.order_by('-upload_date')[:10]

def upload_csv(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("csvFile")

        if not uploaded_file:
            return render(request, "pages/upload.html", {
                "error": "No file uploaded."
            })

        if not uploaded_file.name.endswith(".csv"):
            return render(request, "pages/upload.html", {
                "error": "File must be a .csv file."
            })

        # Build a path: <project_root>/data_migration/cdspecruns
        upload_path = os.path.join(settings.BASE_DIR, "data_migration", "cdspecruns")

        # Make sure folder exists
        os.makedirs(upload_path, exist_ok=True)

        # Save file into that folder
        fs = FileSystemStorage(location=upload_path)
        filename = fs.save(uploaded_file.name, uploaded_file)

        return render(request, "pages/upload.html", {
            "success": f"Uploaded {filename}!"
        })

    return render(request, "pages/upload.html")   

#Edit view, allows the editing of existing objects
def edit(request, pk):
    user = request.user
    if not user.has_perm('cdspec.can_edit'):
       messages.info(request, "You do not have permission to edit this model")
       return HttpResponseRedirect("/cdspec/" + str(pk)) 
    
    #The post statement is the form submit handler. 
    if request.method == 'POST':
        #We first recreate the form object using the request objects.
        form = EditForm(request.POST, instance=get_object_or_404(SpecRun, pk=pk))
        #As long as the form is valid, we proceed to parsing.
        if form.is_valid():
            model = form.save()
            return HttpResponseRedirect(reverse('cdspec:detail', args=(model.id,)))
    else:
        form = EditForm(instance=get_object_or_404(SpecRun, pk=pk))
    return render(request, 'cdspec/edit.html', {'form': form, 'pk':pk})


#Create View, allows the creation of new objects
def create(request):
    user = request.user
    if not user.has_perm('cdspec.can_upload'):
       messages.info(request, "You do not have permission to upload")
       return HttpResponseRedirect("/cdspec/") 

    #The post statement is the form submit handler. 
    if request.method == 'POST':
        #We first recreate the form object using the request objects.
        form = CreateForm(request.POST, request.FILES)
        #As long as the form is valid, we proceed to parsing.
        if form.is_valid():
            #We parse the file into three dictionaries, header, data and indicies all within parsed_dictionary
            try:
               parsed_dictionary = handle_file_upload(request.FILES['source_file'])  
               #We then save the form but don't commit to db yet
               model = form.save(commit=False)
               #We add all the model's fields that are from the parsed dictionary
               date_time_string = parsed_dictionary['header']['DATE'] + " " + parsed_dictionary['header']['TIME']
               model.run_date = datetime.datetime.strptime(date_time_string, "%y/%m/%d %H:%M:%S")
               model.data = parsed_dictionary['data']
               model.data_points = parsed_dictionary['header']['NPOINTS']
               #Setting the x/y header names
               if "XUNITS" in parsed_dictionary['header']: 
                   model.x_units = parsed_dictionary['header']['XUNITS']
               if "YUNITS" in parsed_dictionary['header']:
                   model.y_units = parsed_dictionary['header']['YUNITS']
               if "Y2UNITS" in parsed_dictionary['header']:
                   model.y2_units = parsed_dictionary['header']['Y2UNITS']
               if "Y3UNITS" in parsed_dictionary['header']:
                   model.y3_units = parsed_dictionary['header']['Y3UNITS']
               #print(molar_ellipticity_calculation(parsed_dictionary['data'], model.pathlength, model.protein_concentration, model.number_of_amino_acids, model.degrees_index))
               model.upload_user = user
               model.upload_user_string = user.username
               #Then save the model to the db, here we can return a different view, maybe redirect.
               model.save()
               return HttpResponseRedirect(reverse('cdspec:detail', args=(model.id,)))
            except:
               messages.error(request, 'Unable to parse file, format error')
               return render(request, 'cdspec/create.html', {'form' : form})

    else:
        form = CreateForm()
    return render(request, 'cdspec/create.html', {'form': form,})

#Singular View w/ graph
def detail(request, pk):
    user = request.user
    model = get_object_or_404(SpecRun, pk=pk)
    
    #restrict view access
    if not model.visible_public:
       if (not model.visible_student and not user.has_perm('cdspec.can_view_all')) or (model.visible_student and not user.has_perm('cdspec.can_view_student')):
          messages.info(request, "You do not have permission to access this spec model")
          return HttpResponseRedirect('/cdspec/')

    #Send the model and all of the data points (presented as a list of x, list of y, list of y2, list of y3) to the corresponding template
    return render(request, 'cdspec/detail.html', {'specrun': model, 'x': graph_format(model.data, 0), 'y': graph_format(model.data, 1), 'y2': graph_format(model.data, 2),
    'y3': (graph_format(model.data, 3) if model.y3_units is not None else None), "pk": pk})

#Multi View
def multi(request, pks):

    user = request.user

    if pks == "":
       messages.info(request, "Select table rows to use the Multi-Graph function")
       return HttpResponseRedirect('/cdspec/')

    proteins = []
    for pk in pks.split('/')[:-1]:
        obj = get_object_or_404(SpecRun, pk=pk)
        #view all spec runs
        if user.has_perm('cdspec.can_view_all'):
           proteins.append(obj)
        #view spec runs only if visible to student or public
        elif user.has_perm('cdspec.can_view_student'):
           if obj.visible_student or obj.visible_public:
              proteins.append(obj)
        #only view spec runs visible to public
        else:
           if obj.visible_public:
              proteins.append(obj)
           else:
              messages.info(request, "You do not have permission to access this spec model")
              return HttpResponseRedirect('/cdspec/')

    #check if the models have the same units
    x_units = proteins[0].x_units
    y_units = proteins[0].y_units
    y2_units = proteins[0].y2_units
    y3_units = proteins[0].y3_units
    for protein in proteins:
        if protein.x_units != x_units or protein.y_units != y_units or protein.y2_units != y2_units or protein.y3_units != y3_units:
            messages.info(request, 'Multi-graph failed: graphs have different axes')
            return HttpResponseRedirect('/cdspec/')

    #Send the models and all of the data points (presented as a list of x, list of y, list of y2, list of y3) to the corresponding template
    output_object = [];
    for protein in proteins:
        output_object.append({'run_title' : protein.run_title, 'model' : protein, 'x' : graph_format(protein.data, 0), 'y' : graph_format(protein.data, 1), 'y2' : graph_format(protein.data, 2),
        'y3' : (graph_format(protein.data, 3) if protein.y3_units is not None else None)});

    return render(request, 'cdspec/multi.html', {'proteins': output_object, 'pks': pks, 'first': proteins[0]})

# Table List View
class SpecRunJson(BaseDatatableView):
    model = SpecRun
    
    #filter out models based on logged in user and model visibility
    def get_initial_queryset(self):
        user = self.request.user
        q = SpecRun.objects

        #filter out if looking for models from single upload user
        if self.kwargs:
           q = q.filter(upload_user_string=self.kwargs['user'])

        #view all spec runs
        if user.has_perm('cdspec.can_view_all'):
           return q
        #view spec runs only if visible to student or public
        elif user.has_perm('cdspec.can_view_student'):
           return q.filter(Q(visible_student=True)|Q(visible_public=True))
        #only view spec runs visible to public
        else:
           return q.filter(visible_public=True)
        
    
#Delete view
@require_http_methods(["POST"])
def delete(request, pk):
    user = request.user 
    # fetch the object related to passed id 
    obj = get_object_or_404(SpecRun, id = pk)

    if not user.has_perm('cdspec.can_delete'):
       messages.info(request, "You do not have permission to delete this model")
       return HttpResponseRedirect("/" + str(pk)) 
  
  
    if request.method =="POST": 
        # delete object
        obj.source_file.delete() 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/cdspec/") 
  