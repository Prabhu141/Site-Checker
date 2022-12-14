from django.db import models

#from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Sitemap(models.Model):
    info = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if self.documents:
            self.documents.delete()
            super().delete(*args, **kwargs)
     