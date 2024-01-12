"""toolcrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from core.views import index, about
from userprofile.views import signup
from dashboard import urls as dashboardUrls
from leads import urls as leadsUrls

urlpatterns = [
    path(route='', view=index, name='index'),
    path("dashboard/leads/", include(leadsUrls)),
    path("dashboard/", include(dashboardUrls)),
    path(route='about/', view=about, name='about'),
    path(route='sign-up/', view=signup, name='signup'),
    path(route='login/', view=LoginView.as_view(template_name="userprofile/login.html"), name='login'),
    path(route='logout/', view=LogoutView.as_view(template_name="userprofile/logout.html"), name='logout'),
    path('admin/', admin.site.urls),
]
