from .models import Contact, Reservation
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'subject', 'message']
 


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['customer', 'table_number', 'seats', 'date', 'time']

