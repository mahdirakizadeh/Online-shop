from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='user_sign_up'),
    path('verify/', views.UserSignupVerifyView.as_view(), name='verify_code'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
]
