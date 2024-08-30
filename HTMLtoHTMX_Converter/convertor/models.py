from django.db import models

class HTMLFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='html_files/')
    upload_date = models.DateTimeField(auto_now_add=True)
