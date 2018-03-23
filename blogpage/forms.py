
from django.forms import ModelForm
from blogpage.models import Post
from slugify import slugify


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['theme', 'message', 'rate']

    def get_slugified(self):
        instance = super(PostForm, self).save(commit=False)
        instance.slug = slugify(instance.theme)

        return instance