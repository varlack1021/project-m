from django.urls import path
from . import views


urlpatterns = [
	path('video_links/', views.index, name='index'),
	path('createVideoLink/', views.createVideoLink, name='createVideoLink'),
	path('place_holder/', views.placeHolder, name='placeHolder')
]