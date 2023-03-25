
from django.shortcuts import render,redirect





def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowedGroups:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('user_profile')

        return wrapper_func

    return decorator