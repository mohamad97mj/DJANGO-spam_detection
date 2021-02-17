from .utils import *


class Test(Model):
    precision = CharField(max_length=255)
    recall = IntegerField()

    def __str__(self):
        return self.bio

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



