import datetime

from django.shortcuts import render, get_object_or_404, redirect
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

from django.db.models import Q

# Create your views here.
#The file contains all the views (not ideal)

#Index View, a list of last ten objects
class IndexView(generic.ListView):
    template_name = "cdspec/index.html"
    context_object_name = 'latest_runs'

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        context = {'latest_runs': queryset}

        if kwargs:
            context['username'] = kwargs['user']

        return render(request, 'cdspec/index.html', context)

    def get_queryset(self):
        if self.kwargs:
            user = get_user_model().objects.get(username=self.kwargs['user'])
            return SpecRun.objects.filter(upload_user=user).order_by('-upload_date')[:10]
        else:
            return SpecRun.objects.order_by('-upload_date')[:10]


#Edit view
def edit(request, pk):
    user = request.user
    if not user.has_perm('cdspec.can_edit'):
        messages.info(request, "You do not have permission to edit this model")
        return HttpResponseRedirect("/cdspec/" + str(pk))

    if request.method == 'POST':
        form = EditForm(request.POST, instance=get_object_or_404(SpecRun, pk=pk))
        if form.is_valid():
            model = form.save()
            return HttpResponseRedirect(reverse('cdspec:detail', args=(model.id,)))
    else:
        form = EditForm(instance=get_object_or_404(SpecRun, pk=pk))

    return render(request, 'cdspec/edit.html', {'form': form, 'pk': pk})


#Create View
def create(request):
    user = request.user
    if not user.has_perm('cdspec.can_upload'):
        messages.info(request, "You do not have permission to upload")
        return HttpResponseRedirect("/cdspec/")

    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                parsed_dictionary = handle_file_upload(request.FILES['source_file'])
                model = form.save(commit=False)

                date_time_string = parsed_dictionary['header']['DATE'] + " " + parsed_dictionary['header']['TIME']
                model.run_date = datetime.datetime.strptime(date_time_string, "%y/%m/%d %H:%M:%S")
                model.data = parsed_dictionary['data']
                model.data_points = parsed_dictionary['header']['NPOINTS']

                if "XUNITS" in parsed_dictionary['header']:
                    model.x_units = parsed_dictionary['header']['XUNITS']
                if "YUNITS" in parsed_dictionary['header']:
                    model.y_units = parsed_dictionary['header']['YUNITS']
                if "Y2UNITS" in parsed_dictionary['header']:
                    model.y2_units = parsed_dictionary['header']['Y2UNITS']
                if "Y3UNITS" in parsed_dictionary['header']:
                    model.y3_units = parsed_dictionary['header']['Y3UNITS']

                model.upload_user = user
                model.upload_user_string = user.username
                model.save()

                return HttpResponseRedirect(reverse('cdspec:detail', args=(model.id,)))
            except:
                messages.error(request, 'Unable to parse file, format error')
                return render(request, 'cdspec/create.html', {'form': form})

    else:
        form = CreateForm()

    return render(request, 'cdspec/create.html', {'form': form})


#Singular View w/ graph
def detail(request, pk):
    user = request.user
    model = get_object_or_404(SpecRun, pk=pk)

    if not model.visible_public:
        if (not model.visible_student and not user.has_perm('cdspec.can_view_all')) or \
           (model.visible_student and not user.has_perm('cdspec.can_view_student')):
            messages.info(request, "You do not have permission to access this spec model")
            return HttpResponseRedirect('/cdspec/')

    return render(request, 'cdspec/detail.html', {
        'specrun': model,
        'x': graph_format(model.data, 0),
        'y': graph_format(model.data, 1),
        'y2': graph_format(model.data, 2),
        'y3': (graph_format(model.data, 3) if model.y3_units is not None else None),
        "pk": pk
    })


#Multi View (existing)
def multi(request, pks):
    user = request.user

    if pks == "":
        messages.info(request, "Select table rows to use the Multi-Graph function")
        return HttpResponseRedirect('/cdspec/')

    proteins = []
    for pk in pks.split('/')[:-1]:
        obj = get_object_or_404(SpecRun, pk=pk)

        if user.has_perm('cdspec.can_view_all'):
            proteins.append(obj)
        elif user.has_perm('cdspec.can_view_student'):
            if obj.visible_student or obj.visible_public:
                proteins.append(obj)
        else:
            if obj.visible_public:
                proteins.append(obj)
            else:
                messages.info(request, "You do not have permission to access this spec model")
                return HttpResponseRedirect('/cdspec/')

    x_units = proteins[0].x_units
    y_units = proteins[0].y_units
    y2_units = proteins[0].y2_units
    y3_units = proteins[0].y3_units

    for protein in proteins:
        if protein.x_units != x_units or protein.y_units != y_units or \
           protein.y2_units != y2_units or protein.y3_units != y3_units:
            messages.info(request, 'Multi-graph failed: graphs have different axes')
            return HttpResponseRedirect('/cdspec/')

    output_object = []
    for protein in proteins:
        output_object.append({
            'run_title': protein.run_title,
            'model': protein,
            'x': graph_format(protein.data, 0),
            'y': graph_format(protein.data, 1),
            'y2': graph_format(protein.data, 2),
            'y3': (graph_format(protein.data, 3) if protein.y3_units is not None else None)
        })

    return render(request, 'cdspec/multi.html', {
        'proteins': output_object,
        'pks': pks,
        'first': proteins[0]
    })


# Table List View
class SpecRunJson(BaseDatatableView):
    model = SpecRun

    def get_initial_queryset(self):
        user = self.request.user
        q = SpecRun.objects

        if self.kwargs:
            q = q.filter(upload_user_string=self.kwargs['user'])

        if user.has_perm('cdspec.can_view_all'):
            return q
        elif user.has_perm('cdspec.can_view_student'):
            return q.filter(Q(visible_student=True) | Q(visible_public=True))
        else:
            return q.filter(visible_public=True)


#Delete view
@require_http_methods(["POST"])
def delete(request, pk):
    user = request.user
    obj = get_object_or_404(SpecRun, id=pk)

    if not user.has_perm('cdspec.can_delete'):
        messages.info(request, "You do not have permission to delete this model")
        return HttpResponseRedirect("/" + str(pk))

    if request.method == "POST":
        obj.source_file.delete()
        obj.delete()
        return HttpResponseRedirect("/cdspec/")


# ⭐ NEW MULTI‑SELECT VIEW (added cleanly at the bottom)
def multi_select(request):
    runs = SpecRun.objects.all()
    selected_ids = request.GET.getlist("run_ids")

    if selected_ids:
        ids_param = ",".join(selected_ids)
        return redirect("cdspec:multi", pks=ids_param + "/")

    return render(request, "cdspec/multi.html", {"runs": runs})
