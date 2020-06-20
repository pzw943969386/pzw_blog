from django.urls import path
from liuyan import views

app_name = 'liuyan'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('create/<int:id>',views.create,name='create'),
]