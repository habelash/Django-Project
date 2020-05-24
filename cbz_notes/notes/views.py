from django.shortcuts import render
from .models import notes

def index(request):
    pdfs = notes.objects.all()
    return render(request, "index.html", {'pdfs': pdfs})
# Create your views here.
