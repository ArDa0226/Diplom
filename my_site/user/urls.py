
from django.urls import path
from .views import *

urlpatterns = [
    path('', UserHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('adduser/', AddUser.as_view(), name='add_user'),
    path('contact/', contact, name='contact'),
    path('userinfo/<slug:user_slug>/', ShowUser.as_view(), name='user_inf'),
    path('group/<slug:group_slug>/', UserGroup.as_view(), name='group')

]


