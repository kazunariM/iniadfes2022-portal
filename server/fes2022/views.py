from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.


class QRlistView(ListView):
    model = models.NamecardPool
    template_name = "fes2022/list.html"
    context_object_name = "cards"
    
    def get_queryset(self):
        return models.NamecardPool.objects.filter(used=False).order_by("namecard").order_by("pk")
    