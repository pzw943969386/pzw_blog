from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('edit/<int:id>/', views.profile_edit, name='edit'),
    path('set_password/<int:id>/',views.set_password,name='set_password'),
]