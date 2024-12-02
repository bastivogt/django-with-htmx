from django import forms
from django.utils.translation import gettext as _

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        exclude = [
            "user"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for item in self.fields:
            self.fields[item].label_suffix = ""

        self.fields["title"].label = _("Title")
        self.fields["content"].label = _("Content")
        self.fields["done"].label = _("Done")

        self.fields["title"].widget.attrs["class"] = "form-control"
        self.fields["content"].widget.attrs["class"] = "form-control"
        self.fields["done"].widget.attrs["class"] = "form-check-input"