from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView, View
from accounts.utils.constants import Templates, SuccessMessages, ErrorMessages, Urls
from accounts.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from requests.exceptions import HTTPError
from django.contrib.messages import info
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from accounts.utils.utils import (
    create_user_session_in_request,
    create_user_information_in_database,
    get_current_logged_in_user,
    upload_user_profile_image_to_firebase_storage_and_format_url,
    get_user_localId,
    update_user_data_to_firebase_database,
    serialize_user_form_data,
)
from quickreads.utils.firebase_config import auth
from typing import Any
from ast import literal_eval


class LoginView(FormView):
    template_name = Templates.SIGN_IN.value
    form_class = UserLoginForm
    success_url = reverse_lazy(Urls.HOME_REVERSE.value)

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            create_user_session_in_request(request=self.request, user=user)
            info(self.request, SuccessMessages.LOGIN.value)
            return super().form_valid(form)
        except HTTPError as http_error:

            form.add_error(
                None,
                literal_eval(http_error.strerror)
                .get("error", ErrorMessages.LOGIN.value)
                .get("message", ErrorMessages.LOGIN.value),
            )
            return super().form_invalid(form)
        except Exception as err:
            print(ErrorMessages.UNKNOWN_ERROR.value.format(err=err))
            form.add_error(None, err)
            return super().form_invalid(form)


class RegisterView(FormView):
    template_name = Templates.REGISTER.value
    form_class = UserRegisterForm
    success_url = reverse_lazy(Urls.REGISTER_REVERSE.value)

    def form_valid(self, form):
        try:
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = auth.create_user_with_email_and_password(email, password)
            create_user_information_in_database(user=user, data=form.cleaned_data)
            info(self.request, SuccessMessages.SIGNUP.value)
            return super().form_valid(form)
        except HTTPError as http_error:

            form.add_error(
                None,
                literal_eval(http_error.strerror).get("error").get("message"),
            )
            return super().form_invalid(form)
        except Exception as err:
            form.add_error(None, ErrorMessages.UNKNOWN_ERROR.name.format(err=err))
            return super().form_invalid(form)


class UpdateView(FormView):
    template_name = Templates.PROFILE.value
    form_class = UserUpdateForm
    success_url = reverse_lazy(Urls.UPDATE_REVERSE.value)

    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        try:
            return super().get(request, *args, **kwargs)
        except HTTPError:
            return redirect(reverse_lazy(Urls.LOGOUT_REVERSE.value))

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = get_current_logged_in_user(self.request)
        context["user"] = user
        return context

    def form_valid(self, form):
        form_data = form.cleaned_data
        if form_data.get("profile"):
            profile_url = upload_user_profile_image_to_firebase_storage_and_format_url(
                user=form_data.get("name"), file=form_data.get("profile")
            )
        form_data = serialize_user_form_data(form_data)
        form_data["profile"] = profile_url
        print(form_data)
        localId = get_user_localId(self.request)
        update_user_data_to_firebase_database(localId=localId, data=form_data)
        info(self.request, SuccessMessages.UPDATE.value)
        return super().form_valid(form)


class LogOutView(View):
    def get(self, request):
        logout(request)
        info(request, SuccessMessages.LOGOUT.value)
        return redirect(reverse_lazy(Urls.LOGIN_REVERSE.value))
