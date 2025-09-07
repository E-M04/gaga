from django.db import models
from django.contrib.auth.models import AbstractUser
from gag.helpers import UploadTo

class User(AbstractUser):
    photo=models.ImageField(upload_to=UploadTo('profile'),blank=True,null=True)



    @property
    def image_url(self):
        if self.image and hasattr(self.photo, "url"):  # 👈 .url ni tekshirish
            return self.image.url  # 👈 To'g'ridan-to'g'ri .url ishlating
        return f"{settings.STATIC_URL}img/no_hoto.jpg"  
