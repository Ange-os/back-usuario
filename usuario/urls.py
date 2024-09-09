from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views
from .views import UserListCreateAPIView, PasswordResetResquestview, PasswordResetConfirmView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    #LOGIN
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
        # URL para solicitar restablecer la contraseña
    path('password-reset/', 
        PasswordResetResquestview.as_view(), name='password_reset'),
    
    # URL que confirma el envío del email para restablecer contraseña
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
        name='password_reset_done'),

    # URL para ingresar nueva contraseña desde el email
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
        name='password_reset_confirm'),

    # URL que confirma el restablecimiento exitoso de la contraseña
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
        name='password_reset_complete'),

    path('password-reset-confirm/', 
        PasswordResetConfirmView.as_view(), name='password-reset-confirm'),   
]
