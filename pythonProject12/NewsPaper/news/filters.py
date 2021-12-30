from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms

class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'dateCreation',
            'author',
            'categoryType',
        }