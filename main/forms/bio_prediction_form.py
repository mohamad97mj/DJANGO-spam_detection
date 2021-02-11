from .utils import *


class BioPredictionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].required = False
        self.fields['predicted_label'].required = False
        self.fields['probability'].required = False

    def init_predicted_label(self, predicted_label):
        _mutable = self.data._mutable
        self.data._mutable = True
        self.data['predicted_label'] = predicted_label
        self.data._mutable = _mutable

    def init_probability_label(self, probability):
        _mutable = self.data._mutable
        self.data._mutable = True
        self.data['probability'] = probability
        self.data._mutable = _mutable

    def clean_text(self):
        text = self.cleaned_data.get("text")
        empty_field_validator(text)
        return text

    def save(self, commit=True):
        m = super(BioPredictionForm, self).save(commit=False)
        if commit:
            m.save()
        return m

    class Meta:
        model = Prediction
        fields = [
            'text',
            'predicted_label',
            'probability',
        ]
        labels = {
            'text': "متن مورد بررسی",
            'predicted_label': 'برچسب پیش بینی شده',
            'probability': 'احتمال',
        }
        help_texts = {
        }
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 5}),
            'predicted_label': TextInput(attrs={'disabled': True}),
            'probability': TextInput(attrs={'disabled': True}),
        }
