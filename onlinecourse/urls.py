from django.urls import path
from . import view

app_name = 'onlinecourse'

urlpatterns = [
    path('login', view.login_user, name='login'),
    path('logout', view.logout_user, name='logout'),
]