"""
URL configuration for myProject project.

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
from django.urls import path
from myApp import views 
from django.contrib.auth import views as auth_view
from myApp.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.HandleIndex, name="index"),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product', views.ProductView.as_view(), name='product'),
    path('feature/', views.feature, name='feature'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html', 
        authentication_form = LoginForm), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name = 'logout'),
    path('signup/', views.CustomerRegistratioinView.as_view(), name='signup'),

]
