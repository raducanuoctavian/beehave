from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Title_Tag'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'user name', 'id' : 'elder',
                                              'value' : '', 'type' : 'hidden'}),
            'category' : forms.Select(choices=choice_list, attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Body'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Snippet'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Title_Tag'}),
            # 'author' : forms.Select(attrs={'class' : 'form-control', 'placeholder': 'Author'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Body'}),
            'snippet' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Snippet'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Body'}),
        }
