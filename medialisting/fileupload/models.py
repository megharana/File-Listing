from django.db import models


class FileUpload(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to="files/%Y/%m/%d")
    uploaded_at = models.DateTimeField(auto_now_add=True)