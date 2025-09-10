from django.templatetags.static import static
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import widgets
from gag.helpers import UploadTo
from django.conf import settings

class User(AbstractUser):
    photo=models.ImageField(upload_to=UploadTo('profile'),blank=True,null=True)

    @property
    def image_url(self):
        if self.photo : 
            return self.photo.url
        return static('img/no_photo.jpg')  
    







