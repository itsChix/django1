from django.urls import path
from . import views

urlpatterns = [
    path('showmeeting', views.index, name='all-show')
]
