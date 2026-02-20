# Register your models here.
from django.contrib import admin

from .models import IntegratedMap, Dataset, Tissue, Assay

admin.site.register(IntegratedMap)
admin.site.register(Dataset)
admin.site.register(Tissue)
admin.site.register(Assay)
