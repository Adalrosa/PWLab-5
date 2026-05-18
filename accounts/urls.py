from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),
    path('magic-request/', views.request_magic_link_view, name='magic_request'),
    path('magic-login/<uuid:token>/', views.magic_login_confirm_view, name='magic_login_confirm'),
]