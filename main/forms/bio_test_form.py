from .utils import *


class BioTestForm(ModelForm):
    file = FileField(label="Upload the file of labeled bios")

    field_order = [
        'file',
        'precision',
        'recall',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['precision'].required = False
        self.fields['recall'].required = False
        self.order_fields(field_order=self.field_order)

    def init_precision(self, precision):
        _mutable = self.data._mutable
        self.data._mutable = True
        self.data['precision'] = precision
        self.data._mutable = _mutable

    def init_recall(self, recall):
        _mutable = self.data._mutable
        self.data._mutable = True
        self.data['recall'] = recall
        self.data._mutable = _mutable

    def clean_file(self):
        file = self.cleaned_data.get("file")
        empty_field_validator(file)
        return file

    def save(self, commit=True):
        m = super(BioPredictionForm, self).save(commit=False)
        if commit:
            m.save()
        return m

    class Meta:
        model = Test
        fields = '__all__'
        labels = {
            'precision': "precision",
            'recall': 'recall',
        }
        help_texts = {
        }
        widgets = {
            'precision': TextInput(attrs={'disabled': True}),
            'recall': TextInput(attrs={'disabled': True}),
        }
