from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from web.models import *


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Buyer

class AddForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'name', 'place', 'start_at', 'end_at', 'full_text', 'web_buyer_id']

class NewEvent(ModelForm):
    class Meta:
        model = UserHasEvent
        fields = ['title_events']

