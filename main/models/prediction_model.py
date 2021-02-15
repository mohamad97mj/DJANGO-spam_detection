from .utils import *


class Prediction(Model):
    text = CharField(max_length=1023)
    predicted_label = CharField(max_length=255)
    probability = IntegerField()

    def __str__(self):
        return self.text

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




