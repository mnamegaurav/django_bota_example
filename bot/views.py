from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from .chatterbot import bota
import json

# Create your views here.

class ChatterBotAppView(TemplateView):
    template_name = 'home.html'


class ChatterBotApiView(View):

    def post(self, request, *args, **kwargs):
        input_data = request.POST.get('text')
        response = bota.get_response(input_data)
        response_data = response.serialize()
        return JsonResponse(response_data,status=200)