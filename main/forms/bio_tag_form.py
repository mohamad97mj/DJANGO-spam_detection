from .utils import *


class BioTagForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].required = False
        self.fields['label'].required = False

    def clean_bio(self):
        bio = self.cleaned_data.get("bio")
        empty_field_validator(bio)
        return bio

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
            'bio',
            'label',
        ]
        labels = {
            'bio': "bio",
            'label': 'label',
        }
        help_texts = {
        }
        widgets = {
            'bio': Textarea(attrs={'cols': 80, 'rows': 3}),
        }
