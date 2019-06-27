#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from rest_framework.views import APIView

def alert(request):
	template = loader.get_template('alert/index.html')
	return HttpResponse(template.render({}, request))

class AlertView(APIView):

    def post(self, request):
        print("POST!!")
        pass