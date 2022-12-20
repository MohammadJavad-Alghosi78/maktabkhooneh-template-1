from django.urls import path, include
from website.views import *

urlpatterns = [
    path('', index_view, name='index'),
]

