from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("signup/", views.usersignup, name="signup"),
    path("login/", views.userLogin, name="login"),
    path("logout/", views.userLogout, name="logout"),
    path("resetpassword/", auth_views.PasswordChangeView.as_view(
        template_name = "account/passwordReset.html"), name="resetpassword")
]