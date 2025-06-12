from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = CKEditor5Field('Text', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title