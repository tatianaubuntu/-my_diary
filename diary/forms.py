from django.forms import ModelForm

from diary.models import Entry


class EntryForm(ModelForm):

    class Meta:
        model = Entry
        fields = [
            'title',
            'body',
            'image',
        ]
