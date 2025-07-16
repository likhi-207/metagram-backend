from django.urls import path
from . import views
from .views import login , verify , register
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('verify/', views.verify, name='verify'),

]