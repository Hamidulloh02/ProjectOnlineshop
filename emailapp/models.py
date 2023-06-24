from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class SendEmail(models.Model):
      title = models.CharField(max_length=100)
      poster = models.ImageField(upload_to='images/', blank=True, verbose_name='Products upload image')
      text = RichTextField()
      url = models.URLField()