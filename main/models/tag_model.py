from .utils import *


class Tag(Model):
    id = CharField(max_length=255, primary_key=True)
    text = CharField(max_length=1023)
    label = CharField(max_length=255)

    def __str__(self):
        return self.text

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
