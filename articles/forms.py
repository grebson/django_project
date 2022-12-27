from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Article, Category


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label=_('Title'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    content = forms.CharField(
        label=_('Content'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
        }),
    )
    category = forms.ModelChoiceField(
        label=_('Category'),
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
    )

    class Meta:
        model = Article
        fields = ('title', 'content', 'category')


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )

    class Meta:
        model = Category
        fields = ('name',)
