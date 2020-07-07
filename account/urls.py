from django.urls import path, include
from .views import dashboard, register_user, edit_user_details, ProfileList, ProfileDetail, start_following
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    ## USER MANAGED LOGIN.
    # path("login/", account_login, name="login")

    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    # path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    # path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path("", include("django.contrib.auth.urls")),
    path("register/", register_user, name="register"),
    path("edit/",edit_user_details, name="edit_user_details"),
    path("", dashboard, name="dashboard"),
    path("profiles/", login_required(ProfileList.as_view()), name="profiles"),
    path("profiles/<pk>/", login_required(ProfileDetail.as_view()), name="profile_details"),
    path("start_following/", start_following, name="start_following"),
]