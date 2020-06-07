from django.contrib import admin
from .models import notes, chemisrty

# Register your models here.
admin.site.site_header = "Kishor Publications"
admin.site.register(notes)
admin.site.register(chemisrty)