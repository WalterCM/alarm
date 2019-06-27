
import simpleaudio as sa

from django.http import HttpResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response

def alert(request):
	template = loader.get_template('alert/index.html')
	return HttpResponse(template.render({}, request))

class AlertView(APIView):

    def post(self, request):
        wave_obj = sa.WaveObject.from_wave_file("/usr/share/sounds/alsa/Rear_Center.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

        return Response({})