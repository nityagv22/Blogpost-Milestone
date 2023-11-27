"""
URL configuration for blogpost project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include,path
from user import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('', user_views.homepage, name='home'),
    path('signup/', user_views.signup, name='signup' ),
    path('blogpage/<str:slug>/', user_views.blogpost, name='blogpost'),
    path('blogpage/', user_views.blogpage, name='blogpage'),
    path('login/',auth_views.LoginView.as_view(template_name='loginpage.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logoutpage.html'),name='logout'),
    path('profile/',user_views.profile, name='profile'),
    path('addblog/',user_views.CreateBlog.as_view(), name='createblog'),
    path('update/<int:id>/', user_views.update_blog, name='updateblog'),
    path('delete/<int:id>', user_views.delete_blog, name='deleteblog')
]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
