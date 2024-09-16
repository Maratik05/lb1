
from django.urls import path

from l1.views import index

urlpatterns = [
    path('', index),
]
