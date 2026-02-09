from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from . import views

urlpatterns = [
    path("status", views.status_view),
    path("", views.integrated_map_list),
    path("integrated_maps/", views.integrated_map_list),
    path("tissues", views.tissue_list),
    path("datasets", views.dataset_list),
    path("assays", views.assay_list),
    path("integrated_maps/<uuid:integrated_map_id>/", views.integrated_map_detail),
    path("assays/<str:assayName>/", views.assay_detail),
    path("tissues/<str:tissuetype>/", views.tissue_detail),
    path("datasets/<str:uuid>/", views.dataset_detail),
    path("integrated_maps/tissue/<str:tissuetype>/", views.integrated_maps_by_tissue),
    path("integrated_maps/assay/<str:assayName>/", views.integrated_maps_by_assay),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
