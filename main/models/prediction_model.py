from .utils import *


class Prediction(Model):
    id = CharField(max_length=255, primary_key=True)
    text = CharField(max_length=1023)
    predicted_label = CharField(max_length=255)
    probability = IntegerField()

    def __str__(self):
        return self.text

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




