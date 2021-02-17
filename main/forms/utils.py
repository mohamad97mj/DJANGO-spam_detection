from django.forms import ModelForm, CharField, ValidationError, Textarea, TextInput, Form, FileField
from main.models import Prediction, Tag, Test

EMPTY_FIELD_ERROR_MESSAGE = 'this field can not be empty'


def empty_field_validator(field_value):
    if not field_value:
        raise ValidationError(EMPTY_FIELD_ERROR_MESSAGE)
