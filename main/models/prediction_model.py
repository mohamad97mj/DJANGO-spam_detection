from .utils import *


class Prediction(Model):
    bio = CharField(max_length=1023)
    predicted_label = CharField(max_length=255)
    probability = IntegerField()
    predicted_by = CharField(max_length=255)

    def __str__(self):
        return self.bio

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




