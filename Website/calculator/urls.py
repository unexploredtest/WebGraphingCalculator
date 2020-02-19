from . import views
from django.urls import path

urlpatterns = [

    path('', views.calculator, name='GraphingCalculator'),
    path('register/', views.register, name='register')

]
