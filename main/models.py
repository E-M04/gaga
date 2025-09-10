from django.db import models
from django.db.models import ForeignKey
from django.urls.base import translate_url
from gag.mixins import TranslateMixin
from gag.helpers import UploadTo

class Category(TranslateMixin,models.Model):
    translate_fields=['name']
    name_uz=models.CharField(max_length=50)
    name_ru=models.CharField(max_length=50)
    image=models.ImageField(upload_to=UploadTo('category'))
    def __str__(self):
        return self.name


class Post(models.Model):
    user=models.ForeignKey('client.User',on_delete=models.RESTRICT)
    category=models.ForeignKey('main.Category',on_delete=models.RESTRICT)
    comment=models.TextField(verbose_name='Izoh')
    file=models.FileField(verbose_name='Rasm va vedio', upload_to=UploadTo('Post'))
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    added_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class PostComment(models.Model):
    parent=models.ForeignKey('self',on_delete=models.RESTRICT,null=True,default=None)
    post=models.ForeignKey('main.Post',on_delete=models.RESTRICT)
    user=models.ForeignKey('client.user',on_delete=models.RESTRICT)
    image=models.ImageField(upload_to=UploadTo('comment'))
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




