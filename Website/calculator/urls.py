from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.calculator),                                                 # The Graphing Calculator webpage
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='calculator/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='calculator/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('calculator/', views.calculator, name='GraphingCalculator'),           # The Graphing Calculator webpage, had some problem with the first one 

]
