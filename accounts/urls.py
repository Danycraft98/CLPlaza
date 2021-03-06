from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html', html_email_template_name='registration/password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/<username>', views.user_profile, name='profile'),
]
