from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from users.views import RegisterNewUserView
urlpatterns = [
    path('accounts/login/',LoginView.as_view(template_name='users/registration/login.html'), name='login'),
    path('register/', RegisterNewUserView.as_view(), name='register'),
    path('logout/', logout_then_login, name='logout'),
]

