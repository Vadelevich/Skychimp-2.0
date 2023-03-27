from django import forms

from base.form import StyleFormMixin
from service.models import Customers, Mailing, Message


class CustomerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Customers
        exclude = ['user_create', ]


class MailingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['add_customer'].queryset = Customers.objects.filter(
            user_create=self.request)
        self.fields['add_message'].queryset = Message.objects.filter(
            user_create=self.request)

    STATUSES = (
        ('completed', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена'),
    )
    state_mail = forms.ChoiceField(choices=STATUSES, )

    class Meta:
        model = Mailing
        exclude = ['user_create', ]


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['user_create', ]
