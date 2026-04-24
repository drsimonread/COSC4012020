from django.urls import path, re_path

from cdspec import views
from .views import SpecRunJson

app_name = 'cdspec'

urlpatterns = [
    # /cdspec/
    path('', views.IndexView.as_view(), name='index'),

    # /cdspec/uploadedby=<username>/
    path('uploadedby=<str:user>/', views.IndexView.as_view(), name='userindex'),

    # /cdspec/create/
    path('create/', views.create, name='create'),

    # /cdspec/<pk>/
    path('<int:pk>/', views.detail, name='detail'),

    # /cdspec/<pk>/edit
    path('<int:pk>/edit/', views.edit, name='edit'),

    # /cdspec/<pk>/delete
    path('<int:pk>/delete/', views.delete, name='delete'),

    # NEW comma‑separated multi view
    path('multi/<str:pks>/', views.multi, name='multi'),

    # /cdspec/ table data
    re_path(r'^spec_run_data/$', SpecRunJson.as_view(), name="spec_run_list_json"),
    path('spec_run_data/<str:user>/', SpecRunJson.as_view(), name="spec_run_list_json_user"),

    # NEW multi-select checkbox page
    path('multi-select/', views.multi_select, name='multi_select'),
]
