"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from django.urls import path

from users.views import ProfileView, RegisterView, email_verification, ResetPassword

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name="Login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirm/<str:verification_code>/', email_verification, name='email-confirm'),
    path('reset/', ResetPassword.as_view(), name='reset'),
    path('profile/', ProfileView.as_view(), name='profile')
]

