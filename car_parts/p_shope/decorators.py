from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext as _


def anonymous_user(function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return function(request, *args, **kwargs)
    return wrapper_function


def vendor_required(function):
    def wrapper_function(request, *args, **kwargs):
        if not request.user.is_vendor:
            messages.warning(request, _("You do NOT have required permissions to view the content."))
            return redirect('/')
        return function(request, *args, **kwargs)
    return wrapper_function


def buyer_required(function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_vendor:
            messages.warning(request, _("You do NOT have required permissions to view the content."))
            return redirect('/')
        return function(request, *args, **kwargs)
    return wrapper_function
