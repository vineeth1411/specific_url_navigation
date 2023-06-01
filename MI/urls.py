from django.urls import path
from MI.views import *
app_name='MI'
urlpatterns = [
    path('rohit/',rohit,name='rohit'),
]
