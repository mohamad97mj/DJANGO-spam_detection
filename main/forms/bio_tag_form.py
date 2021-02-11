from .utils import *


class BioTagForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_text(self):
        text = self.cleaned_data.get("text")
        empty_field_validator(text)
        self.fields['text'].required = False

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
