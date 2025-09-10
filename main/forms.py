from django import  forms
from .models import Post


class PostUpload(forms.ModelForm):
    class Meta:
        model=Post
        fields=['category','comment','file']

