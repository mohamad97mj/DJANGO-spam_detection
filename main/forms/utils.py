from django.forms import ModelForm, CharField, ValidationError, Textarea, TextInput, Form, FileField
from main.models import *

EMPTY_FIELD_ERROR_MESSAGE = 'خطا: این فیلد نمی تواند خالی باشد!'


def empty_field_validator(field_value):
    if not field_value:
        raise ValidationError(EMPTY_FIELD_ERROR_MESSAGE)
