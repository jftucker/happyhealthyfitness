from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.urls import reverse_lazy

from articles.models import Article
from .forms import ContactForm

from django.core.mail import EmailMessage, BadHeaderError, EmailMultiAlternatives
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
            html_content = "<h1><a href=\"happyhealthy.fitness\">Happy Healthy Fitness</a></h1><p>We are so happy that you've decided to start a new fit lifestyle! Be sure to verify your email with us and join the mailing list for updates and support on your journey!</p>"
            '''
            try:
                email = EmailMultiAlternatives(
                    subject,
                    message,
                    from_email,
                    [to_email],
                )
                email.attach_file('static/images/logo.png')
                email.attach_alternative(html_content, "text/html")
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Check your email for our eBook!")
            '''
            new_user = get_user_model().objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                from_frontpage=True,
                on_newsletter=form.cleaned_data['mailer'],   
            )   
            return redirect('home')