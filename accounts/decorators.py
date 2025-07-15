from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def role_required(allowed_roles):
    """Restrict view access to users whose `role` is in `allowed_roles`."""
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if getattr(request.user, 'role', None) not in allowed_roles:
                return HttpResponseForbidden("You do not have permission to access this page.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
