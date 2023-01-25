import datetime

from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from service.models import Customers, Mailing, Message, TryMail
from django.core.mail import send_mail


def statistic(request):
    context = {
        'object_list':TryMail.objects.all()
    }
    return render(request, 'service/statistic.html',context)

class CustomerListView(ListView):
    model = Customers


class MailingListView(ListView):
    model = Mailing


class MessageListView(ListView):
    model = Message


class CustomerCreateView(CreateView):
    model = Customers
    fields = '__all__'
    success_url = reverse_lazy('service:service')


class MailingCreateView(CreateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('service:mail')


class MessageCreateView(CreateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('service:message')


class CustomerUpdateView(UpdateView):
    model = Customers
    fields = '__all__'
    success_url = reverse_lazy('service:service')


class MessageUpdateView(UpdateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('service:message')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('service:mail')


class CustomerDeleteView(DeleteView):
    model = Customers
    success_url = reverse_lazy('service:service')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('service:message')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('service:mail')


class CustomerDetailView(DetailView):
    model = Customers


class MailingDetailView(DetailView):
    model = Mailing


class MessageDetailView(DetailView):
    model = Message


def mail_customer(request):
    mailing_item = Mailing.objects.all()
    for item in mailing_item:
        if (
                item.state_mail == Mailing.STATUSE_CREATED or item.state_mail == Mailing.STATUSE_LAUNCHED) and item.first_date == datetime.date.today() and item.last_date >= datetime.date.today() and item.time_mailing >= datetime.datetime.now().time():
            item.state_mail = Mailing.STATUSE_LAUNCHED
            item.save()
            try:
                res = send_mail(
                    subject=item.add_message.topic_message,
                    message=item.add_message.letter,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[item.add_customer.email],
                    fail_silently=False

                )

                if res:
                    item.state_mail = Mailing.STATUSE_COMPLETED
                    item.save()
                TryMail.objects.create(
                    status=item.state_mail,
                    answer=200,
                )
            except Exception as err:
                TryMail.objects.create(
                    status=item.state_mail,
                    answer=err,
                )

    return redirect(reverse('service:mail'))
