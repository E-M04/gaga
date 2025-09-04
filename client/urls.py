from django.urls import path,include
from .views import create_post
app_name='client'


urlpatterns = [
    path('registration/',create_post,name='create')
]