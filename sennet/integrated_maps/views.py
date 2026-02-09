from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import IntegratedMap, Tissue, Assay


def index(request):
    tissue_list = Tissue.objects.order_by("tissuetype")
    assay_list = Assay.objects.order_by("assayName")
    latest_integrated_map_list=[]
    for t in tissue_list:
        for a in assay_list:
            latest_integrated_map_t=IntegratedMap.objects.filter(tissue=t, assay=a).order_by("-creation_time")
            if(len(latest_integrated_map_t)>0):
                latest_integrated_map_list.append(latest_integrated_map_t[0])
    template = loader.get_template("integrated_maps/index.html")
    context = {
        "latest_integrated_map_list": latest_integrated_map_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, integrated_map_id):
    map = get_object_or_404(IntegratedMap, pk=integrated_map_id)
    assay = map.assay

    if assay.assayName=="rna-seq" or assay.assayName=="multiome-rna-atac":
        template = loader.get_template("integrated_maps/rna-detail.html")
    elif assay.assayName=="atac":
        template = loader.get_template("integrated_maps/atac-detail.html")
    elif assay.assayName=="codex":
        template = loader.get_template("integrated_maps/codex-detail.html")
    else:
        template = loader.get_template("integrated_maps/detail.html")

    context = {"map": map,}
    return HttpResponse(template.render(context, request))


def detail_latest(request, tissuecode, assayName):
    tissue = Tissue.objects.filter(tissuecode=tissuecode)
    assay = Assay.objects.filter(assayName=assayName)
    try:
        latest_integrated_map = IntegratedMap.objects.filter(
            tissue__in=tissue, 
            assay__in=assay
        ).order_by("-creation_time")[0]
    except IndexError:
        raise Http404("Integrated map not found for the specified tissue and assay.")
    context = {"map": latest_integrated_map}
    if assayName in ["rna-seq", "multiome-rna-atac"]:
        template = loader.get_template("integrated_maps/rna-detail.html")
    elif assayName == "atac":
        template = loader.get_template("integrated_maps/atac-detail.html")
    elif assayName == "codex":
        template = loader.get_template("integrated_maps/codex-detail.html")
    else:
        template = loader.get_template("integrated_maps/detail.html")

    return HttpResponse(template.render(context, request))


def tissue(request, tissuetype):

    tissue = Tissue.objects.filter(tissuetype=tissuetype)
    tissue_integrated_map_list = IntegratedMap.objects.filter(tissue__in=tissue.all()).order_by("-creation_time")
    template = loader.get_template("integrated_maps/index.html")
    context = {
        "latest_integrated-map_list": tissue_integrated_map_list,
    }
    return HttpResponse(template.render(context, request))
