from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag('templatetags/articles/categories_dropend_button.html', takes_context=True)
def categories_dropend_button(context):
    categories = Category.objects.all()
    user = context['request'].user

    print(user)
    return {
        'categories': categories,
        'user': user,
    }
