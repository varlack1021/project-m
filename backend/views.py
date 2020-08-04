from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from pprint import pprint

from . import pubsub
from django.http import HttpResponse
from .models import Video 

from bs4 import BeautifulSoup

import re
import sys
import json
# Create your views here.

def index(request):
	videos = Video.objects.all()
	videos = serialize('json', videos)
	return HttpResponse(videos, content_type="application/json")

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.

#Add a video link from the frontend
@csrf_exempt
def createVideoLink(request):
	params = json.loads(request.body)
	video = Video(video_link=params['video_link'])
	video.save()
	dict_video = model_to_dict(video)
	serialized = json.dumps(dict_video)

	return HttpResponse(serialized, content_type="application/json")

# Add a vido linked using an endpoint
@csrf_exempt
def placeHolder(request):
	body = request.POST
	subject = body['subject']
	html =body['html']

	sender = json.loads(body['envelope'])['from']
	html_parsed = BeautifulSoup(html, 'html.parser')
	
	all_links = re.findall("(https?://[^\s]+)", html_parsed.text)
	
	for link in all_links:
		video = Video(video_link=link)
		video.save()	

	return HttpResponse(status=200)
