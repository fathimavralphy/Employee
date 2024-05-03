from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from base.views import home,index
from .views import logout_view, RegisterView, add_employee

urlpatterns = [
    path('',index,name="index.html"),
    path("accounts/profile/",home,name="home"),
    # path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',logout_view,name='logout'),
    path('add/', add_employee,name='add_employee'),
    path('register/', RegisterView.as_view(), name='register'),

]