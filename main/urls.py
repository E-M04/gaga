from django.urls import path,include
from .views import index,upload_post,post_like
app_name='main'


urlpatterns = [
    path('',index,name='index'),
    path('upload/',upload_post,name='upload'),
    path('cat/<int:id>',upload_post,name='cat'),
    path('post/<int:post_id>/<str:action>/',post_like,name='post_like')
]

