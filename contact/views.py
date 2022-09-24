# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Contact
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Contact(View):
    """
    This view displays the contact form and if the user
    is registered and inserts the user email into the
    email field
    """
    template_name = 'contact/contact.html'
    success_message = 'Message has been sent.'

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email input
        """
        if request.user.is_authenticated:
            email = request.user.email
            contact_form = ContactForm(initial={'email': email})
        else:
            contact_form = ContactForm()
        return render(request, 'contact/contact.html',
                      {'contact_form': contact_form})

    def post(self, request):
        """
        Checks that the provided info is valid format
        and then posts to database
        """
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(
                request, "Message has been sent")
            return render(request, 'contact/contact.html')

        return render(request, 'contact/contact.html',
                      {'contact_form': contact_form})
