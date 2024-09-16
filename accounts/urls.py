from django.urls import path, include
from accounts.views import LoginView, LogOutView, RegisterView, UpdateView
from accounts.utils.constants import Urls

urlpatterns = [
    path("login/", LoginView.as_view(), name=Urls.LOGIN_REVERSE.value),
    path("register/", RegisterView.as_view(), name=Urls.REGISTER_REVERSE.value),
    path("logout/", LogOutView.as_view(), name=Urls.LOGOUT_REVERSE.value),
    path("profile/", UpdateView.as_view(), name=Urls.UPDATE_REVERSE.value),
]
