from django.urls import path
from LSG.views import *
app_name='LSG'
urlpatterns = [
    path('raahul/',raahul,name='raahul'),
]
