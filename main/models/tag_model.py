from .utils import *


class Tag(Model):
    text = CharField(max_length=1023)
    label = CharField(max_length=255, choices=Labels.choices, default=Labels.APPROPRIATE)

    def __str__(self):
        return self.text

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
