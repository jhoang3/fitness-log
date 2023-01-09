from django.forms import ModelForm, Textarea
from item.models import Entry

class EntryForm(ModelForm): # take in metadata to create a form. All the fields are based off model of Entry
    class Meta: 
        model = Entry
        fields = {
            'title',
            'routine'
        }
        widgets = {
            'routine': Textarea()
        }
        