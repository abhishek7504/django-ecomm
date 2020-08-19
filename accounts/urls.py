from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.user_logout,name='user_logout'),
]