from django import forms
from quickreads.utils.constants import Constants, Employees


class Book(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": Constants.FORM_CLASS.value, "required": True}
        ),
        label="Book Title",
    )
    description = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": Constants.FORM_CLASS.value, "required": True}
        ),
        label="Description",
    )
    authors = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": Constants.FORM_CLASS.value, "required": True}
        ),
        label="Author",
    )
    published = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": Constants.FORM_CLASS.value,
                "required": True,
                "type": "date",
                "id": "datePickerId",
            }
        ),
        label="Published",
    )
    cover = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                "class": Constants.FORM_CLASS.value,
                "required": True,
                "type": "file",
                "accept": "image/*",
            }
        ),
        label="Book Cover",
    )
    book = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                "class": Constants.FORM_CLASS.value,
                "required": True,
                "type": "file",
                "accept": "application/pdf",
            }
        ),
        label="Book",
    )


class Themes(forms.Form):
    theme = forms.ChoiceField(
        choices=Constants.THEME_CHOICES.value,
        widget=forms.Select(
            attrs={
                "class": "select select-bordered w-full select-sm",
                "id": "themeSelect",
                "required": False,
            }
        ),
    )


class NewsLetter(forms.Form):
    subscribe = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "grow", "type": "email"})
    )
