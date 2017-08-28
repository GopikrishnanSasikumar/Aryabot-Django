from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
class ChatterBotAppView(TemplateView):
    template_name = "app.html"
