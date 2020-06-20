"""pzwblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from article import views
from article.views import article_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_list, name='home'),
    path('article/',include('article.urls', namespace='article')),
    path('user/', include('user.urls', namespace='user')),
    path('password_reset/', include('password_reset.urls')),
    path('comment/', include('comment.urls', namespace='comment')),
    path('liuyan/',include('liuyan.urls',namespace='liuyan')),
    path('about/',views.about,name='about')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)