from django.db.models import Model, CharField, IntegerField, TextChoices, AutoField
from django.utils.translation import gettext_lazy as _


class Labels(TextChoices):
    APPROPRIATE = "appropriate", _('مناسب')
    INAPPROPRIATE = "inappropriate", _('نامناسب')

# def init_from_json(self, args, kwargs):
#     for key in args[0]:
#         setattr(self, key, args[0][key])
#     for key in kwargs:
#         setattr(self, key, kwargs[key])
