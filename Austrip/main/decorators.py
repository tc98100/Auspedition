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
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_groups:
                return view(request, *args, **kwargs)
            else:
                return HttpResponse('Nah mate you can go here :(')
        return wrapper
    return decorator

