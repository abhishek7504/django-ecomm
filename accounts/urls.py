from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('register/complete/',views.register_complete,name='register_complete'),
]