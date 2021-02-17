from .utils import *


class BioBulkTagForm(Form):
    file = FileField(label="upload the file of labeled bios")
