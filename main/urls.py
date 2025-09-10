from django.urls import path,include
from .views import index,upload_post
app_name='main'


urlpatterns = [
    path('',index,name='index'),
    path('upload/',upload_post,name='upload')
]

