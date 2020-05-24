from django.db import models


# Create your models here.
class notes(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name
