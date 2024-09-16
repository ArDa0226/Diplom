
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import title
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *
# Create your views here.




class UserHome(DataMixin, ListView):
    model = User
    template_name = 'user/index.html'
    context_object_name = 'users'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))



# def index(request):
#     users = User.objects.all()
#         # groups = Group.objects.all()
#     context = {
#         'users': users,
#         # 'groups': groups,
#         'menu': menu,
#         'title': 'Главная страница',
#         'group_selected': 0,
#     }
#     return render(request, 'user/index.html', context=context)

def about(request):
    return render(request, 'user/about.html', { 'menu': menu, 'title': 'О сайте'})

class AddUser(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddUserForm
    template_name = 'user/adduser.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление сотрудника')
        return dict(list(context.items()) + list(c_def.items()))


# def adduser(request):
#     if request.method == 'POST':
#         form = AddUserForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddUserForm()
#     return render(request, 'user/adduser.html', {'form':form, 'menu': menu, 'title': 'Добавление пользователя'})

def contact(request):
    return HttpResponse('Обратная связь')

class ShowUser(DataMixin, DetailView):
    model = User
    template_name = 'user/user.html'
    slug_url_kwarg = 'user_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['user'])
        return dict(list(context.items()) + list(c_def.items()))

# def show_user(request, user_slug):
#     user = get_object_or_404(User, slug=user_slug)
#
#     context = {
#         'user': user,
#         'menu': menu,
#         'title': user.name,
#         'group_selected': user.group_id,
#     }
#     return render(request, 'user/user.html', context=context)

class UserGroup(DataMixin, ListView):
    model = User
    template_name = 'user/index.html'
    context_object_name = 'users'
    allow_empty = False

    def get_queryset(self):
        return User.objects.filter(group__slug=self.kwargs['group_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Группа - ' + str(context['users'][0].group),
                                      group_selected=context['users'][0].group_id)
        return dict(list(context.items()) + list(c_def.items()))

# def show_group(request, group_id):
#     users = User.objects.filter(group_id=group_id)
#     # groups = Group.objects.all()
#
#     if len(users) == 0:
#         raise Http404()
#
#     context = {
#         'users': users,
#         # 'groups': groups,
#         'menu': menu,
#         'title': 'Пользователи группы',
#         'group_selected': group_id,
#     }
#     return render(request, 'user/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')