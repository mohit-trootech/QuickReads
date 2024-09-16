from django.http import JsonResponse
from django.views.generic import FormView, TemplateView, View
from quickreads.utils.constants import EmailConstants, Templates, SuccessMessages
from quickreads.forms import BookForm
from django.urls import reverse_lazy
from quickreads.utils.constants import Urls
from time import time
from math import floor
from quickreads.utils.utils import (
    serialize_form_data,
    upload_image_to_firebase_storage_and_format_url,
    create_database_snapshot_for_employees,
    get_books_data_snapshot,
    send_mails,
    push_email_newsletter_database,
)
from typing import Any


class HomeView(TemplateView):
    template_name = Templates.BOOKS_LIST.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["books"] = get_books_data_snapshot()
        return context


class BooksView(TemplateView):
    template_name = Templates.BOOKS_LIST.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["books"] = get_books_data_snapshot()
        return context


class CreateBookView(FormView):
    template_name = Templates.ADD.value
    form_class = BookForm
    success_url = reverse_lazy(Urls.HOME_REVERSE.value)

    def form_valid(self, form):

        try:
            data = form.cleaned_data
            key = floor(time())
            cover = upload_image_to_firebase_storage_and_format_url(
                key=key, file=data.get("cover")
            )
            book = upload_image_to_firebase_storage_and_format_url(
                key=key, file=data.get("book")
            )

            data = serialize_form_data(form_data=data, cover=cover, book=book)
            response = create_database_snapshot_for_employees(key=key, data=data)
            return super().form_valid(form)
        except Exception as err:
            form.add_error(None, err)
            return super().form_invalid(form)


class NewsletterView(View):

    def post(self, request):
        email = request.POST.get("email")
        send_mails(
            subject=EmailConstants.NEWSLETTER.value,
            sender=EmailConstants.HOST.value,
            receiver=[email],
            body="Temp Body",
            attachment=None,
        )
        push_email_newsletter_database(email=email)
        return JsonResponse({"message": SuccessMessages.NEWSLETTER.value})
