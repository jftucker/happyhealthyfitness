from django.views.generic import ListView
from django.contrib import messages
from django.views.generic import ListView
from django.urls import reverse_lazy

from articles.models import Article
from .forms import ContactForm

from django.core.mail import EmailMessage, BadHeaderError
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
            subject = 'Thanks for joining the happyhealthy.fitness family!'
            to_email = form.cleaned_data['email']
            from_email = 'Tucker at HHF <tucker@happyhealthy.fitness>'
            message = "We are so happy that you've decided to start a new fit lifestyle! Be sure to verify your email with us and join the mailing list for updates and support on your journey!"
            try:
                email = EmailMessage(
                    subject,
                    message,
                    from_email,
                    [to_email],
                )
                email.attach_file('static/images/logo.png')
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Check your email for our eBook!")
            return redirect('home')