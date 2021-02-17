from main.models import *
from django.http import Http404


def load_tag(pk):
    try:
        return Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        raise Http404


def load_tags():
    return Tag.objects.all()
