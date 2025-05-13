"""
URL configuration for gbrs project.

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
from django.urls import path,include
from system.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('search/',search,name='search'),
    path('login/',login_page,name='login_page'),
    path('signup/',signup_page,name='signup_page'),
    path('tickets/',tickets,name='tickets'),
    path('logout/',logout_page,name='logout_page'),
    path('booking/<id>',booking,name='booking'),
    path('account/',account,name='account'),
    path('delete_account/',delete_account,name='delete_account'),
    path('booking/confirm/',confirm,name='confirm'),
    path('booking/confirmed/<id>',render_pdf_view,name='render_pdf_view'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "resetpassword.html"),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = "resetpasswordsent.html"),name='password_reset_done'),    
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = "resetpasswordform.html"),name='password_reset_confirm'),
    path('reset_password_success/',auth_views.PasswordResetCompleteView.as_view(template_name = "resetpasswordcomplete.html"),name='password_reset_complete'),
    path("__reload__/", include("django_browser_reload.urls")),
]
