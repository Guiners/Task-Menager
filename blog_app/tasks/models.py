from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.CharField(max_length=400, verbose_name=_("Description"))
    completed = models.BooleanField(default=False, verbose_name=_("Completed"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        return self.title

    def clean(self):
        if not self.title:
            raise ValidationError(_("Title is required"))
