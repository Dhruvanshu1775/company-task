from django.urls import path
from .views import *

urlpatterns = [
    path('insert/', UploadCSV.as_view(),name='insert')
]