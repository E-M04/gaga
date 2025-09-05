from django.urls import path,include
from .views import create_post,user_login,client_logout
app_name='client'


urlpatterns = [
    path('registration/',create_post,name='registration'),
    path('login/',user_login,name='login'),
    path('logout/',client_logout,name='logout')
]