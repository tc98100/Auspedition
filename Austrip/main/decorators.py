from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view):

    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view(request, *args, **kwargs)

    return wrapper


def allowed_users(allowed_groups=[]):
    def decorator(view):
        def wrapper(request, *args, **kwargs):
            return view(request, *args, **kwargs)
        return wrapper
    return decorator

