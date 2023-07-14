from django import forms

class LocationForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    detailing_type = forms.ChoiceField(choices=(
        ('current', 'Current weather'),
        ('hourly', 'Hourly forecast'),
        ('daily', 'Daily forecast'),
    ))