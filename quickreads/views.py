from django.views.generic import FormView, TemplateView
from quickreads.utils.constants import Templates
from quickreads.forms import Book
from django.urls import reverse_lazy
from quickreads.utils.constants import Urls
from time import time
from math import floor
from django.http import HttpRequest, HttpResponse
from django.contrib.messages import info
from quickreads.utils.utils import (
    serialize_form_data,
    upload_image_to_firebase_storage_and_format_url,
    create_database_snapshot_for_employees,
    get_books_data_snapshot,
)
from quickreads.utils.firebase_config import *
from typing import Any

# def home(request):
# 	day = database.child('Data').child('Day').get().val()
# 	id = database.child('Data').child('ID').get().val()
# 	projectname = database.child('Data').child('Project').get().val()
# 	return render(request,"home.html",{"day":day,"id":id,"projectname":projectname })


class HomeView(TemplateView):
    template_name = Templates.BOOKS_LIST.value


class BooksView(TemplateView):
    template_name = Templates.BOOKS_LIST.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["books"] = get_books_data_snapshot()
        return context


class CreateBookView(FormView):
    template_name = Templates.ADD.value
    form_class = Book
    success_url = reverse_lazy(Urls.HOME_REVERSE.value)

    def form_valid(self, form):

        try:
            data = form.cleaned_data
            key = floor(time())
            file_url = upload_image_to_firebase_storage_and_format_url(
                key=key, file=data.get("file")
            )
            data = serialize_form_data(form_data=data, file_url=file_url)
            response = create_database_snapshot_for_employees(key=key, data=data)
            print(response)
            return super().form_valid(form)
        except Exception as err:
            form.add_error(None, err)
            return super().form_invalid(form)
