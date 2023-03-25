from django.urls import path
from accounts.views import RegisterView, logout_view, LoginView, PersonalAccount, UserChangeView, UserPasswordChange

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('personal_account/<int:pk>/', PersonalAccount.as_view(), name='personal'),
    path('personal_account/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('personal_account/<int:pk>/change/passwod', UserPasswordChange.as_view(), name='change_password')
]
