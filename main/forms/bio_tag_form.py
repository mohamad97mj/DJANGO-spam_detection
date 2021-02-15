from .utils import *


class BioTagForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].required = False
        self.fields['label'].required = False

    def clean_text(self):
        text = self.cleaned_data.get("text")
        empty_field_validator(text)
        return text

    def clean_label(self):
        label = self.cleaned_data.get("label")
        empty_field_validator(label)
        return label

    def save(self, commit=True):
        m = super(BioTagForm, self).save(commit=False)
        if commit:
            m.save()
        return m

    class Meta:
        model = Tag
        fields = [
            'text',
            'label',
        ]
        labels = {
            'text': "متن مورد نظر",
            'label': 'بر چسب',
        }
        help_texts = {
        }
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
