from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from articles.models import Article
from .forms import ContactForm

from django.core.mail import EmailMessage, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect

from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation


class HomePageView(ListView):
    model = Article
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_articles'] = self.model.objects.all()
        try:
            old_contact_form = self.request.session['contact_form']
        except:
            old_contact_form = None
        context['contact_form'] = ContactForm
        return context

    def post(self, request, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            new_user = get_user_model().objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
            )
            new_user.from_frontpage=True
            new_user.on_newsletter=form.cleaned_data['mailer']
            new_user.save()
            
            EmailAddress.objects.create(user=new_user, email=new_user.email, primary=True, verified=False)
            send_email_confirmation(request, new_user)

            return redirect('ebook')


class EbookPageView(TemplateView):
    template_name = 'ebook_download.html'