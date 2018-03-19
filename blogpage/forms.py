
from django.forms import ModelForm
from blogpage.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['slug', 'theme', 'user', 'message', 'rate']