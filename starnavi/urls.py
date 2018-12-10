"""starnavi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from core import views as core_views
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib.auth import views as auth_views

from likes.views import LikesViewSet
from posts.views import PostsViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'likes', LikesViewSet)
router.register(r'posts', PostsViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^signup_json/$', core_views.SignUpView.as_view(), name='signup_json'),
    url(r'^$', core_views.front, name='front'),
    url(r'^signup/$', core_views.signup, name='core_signup'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'core/login.html',
         'redirect_field_name': 'front'}, name='core_login'),
    url(r'^logout/$', auth_views.logout, name='core_logout'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),

]
