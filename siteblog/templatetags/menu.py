from django import template
from siteblog.models import Category

register = template.Library()


# создание своего тега
@register.inclusion_tag('menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {
        "categories": categories,
        "menu_class": menu_class,
    }
