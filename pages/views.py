from django.views.generic import ListView
from django.contrib import messages
from django.views.generic import ListView
from django.urls import reverse_lazy

from articles.models import Article
from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect


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
            subject = form.cleaned_data['name'] + ' sent a message through hire.johntucker.me!'
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['hire@johntucker.me'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your message was sent!')
            return redirect('home')