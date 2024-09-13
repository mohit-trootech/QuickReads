from django.views.generic import FormView, View
from accounts.utils.constants import Templates, SuccessMessages, ErrorMessages, Urls
from accounts.forms import UserLoginForm, UserRegisterForm
from quickreads.utils.firebase_config import *
from requests.exceptions import HTTPError
from django.contrib.messages import info
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from accounts.utils.utils import (
    create_user_session_in_request,
    create_user_information_in_database,
)


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
        except HTTPError:
            form.add_error(None, ErrorMessages.LOGIN.value)
            return super().form_invalid(form)
        except Exception as err:
            print(f"Other error occurred: {err}")
            form.add_error(None, err)
            return super().form_invalid(form)


class RegisterView(FormView):
    template_name = Templates.REGISTER.value
    form_class = UserRegisterForm
    success_url = "/accounts/login/"

    def form_valid(self, form):
        try:
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = auth.create_user_with_email_and_password(email, password)
            create_user_information_in_database(user=user, data=form.cleaned_data)
            info(self.request, SuccessMessages.SIGNUP.value)
            return super().form_valid(form)
        except Exception as err:
            from pprint import pp

            pp(err.__dict__)
            form.add_error(None, f"Other error occurred: {err}")
            return super().form_invalid(form)


class LogOutView(View):
    def get(self, request):
        logout(request)
        info(request, SuccessMessages.LOGOUT.value)
        return redirect(reverse_lazy(Urls.LOGIN_REVERSE.value))
