from django.shortcuts import render
from .models import Meeting, Location, Participant
# Create your views here.

def index(request):
    meeting = Meeting.objects.all()
    return render(request, "templates/index.html", {"meeting" : "meeting"})