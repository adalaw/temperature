from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('graph/<int:id>', graph, name='graph'),
    path('upload', upload_file, name='upload'),
]