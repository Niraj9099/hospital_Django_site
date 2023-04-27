from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('signup/', views.Ragisterform, name='signup'),
    path('login/', views.LoginForm, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.logout_user, name='logout')



]
