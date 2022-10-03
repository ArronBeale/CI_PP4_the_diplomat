# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# This will get the user information


def get_user_instance(request):
    """
    retrieves user details if logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


# Displays the contact form for the user, autofills their email,
# checks all data is valid before saving it


class ContactMessage(View):
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
            return render(request, 'contact/received.html')

        return render(request, 'contact/contact.html',
                      {'contact_form': contact_form})
