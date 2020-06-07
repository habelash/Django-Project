from django.shortcuts import render
from .models import notes, chemisrty


def index(request):
    context = {
        "pdfs": notes.objects.all(),
        "chem": chemisrty.objects.all()
    }

    return render(request, "index.html", context)
# Create your views here.
