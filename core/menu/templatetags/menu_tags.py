from django import template
from menu.models import Item, Category

register = template.Library()



@register.inclusion_tag('menu/popular-item.html')
def popularposts():
    items = Item.objects.filter(is_available=True).order_by('-score')[0:6]
    print(items)
    print(items.count())
    return {'items':items}