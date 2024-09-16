from django import template
from user.models import *

register = template.Library()

@register.simple_tag()
def get_groups(filter=None):
    if not filter:
        return Group.objects.all()
    else:
        return Group.objects.filter(pk=filter)

@register.inclusion_tag('user/list_groups.html')
def show_groups(sort=None, group_selected=0):
    if not sort:
        groups = Group.objects.all()
    else:
        groups = Group.objects.order_by(sort)
    return {'groups': groups, 'group_selected': group_selected}