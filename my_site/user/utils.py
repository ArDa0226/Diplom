from django.db.models import Count

from .models import *

menu = [{'title': 'О сайте', 'url_name':'about'},
        {'title': 'Добавить сотрудника', 'url_name':'add_user'},
        {'title': 'Обратаная связь', 'url_name': 'contact'}]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        groups = Group.objects.annotate(Count('user'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['groups'] = groups
        if 'group_selected' not in context:
            context['group_selected'] = 0
        return context