from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ChatterBotAppView(TemplateView):
    template_name = "app.html"
