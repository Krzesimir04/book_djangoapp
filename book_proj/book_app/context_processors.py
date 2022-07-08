from django.contrib.auth.models import User
from .models import Visit
def is_reservation(request):
    if request.user.is_authenticated:
        visits=Visit.objects.filter(User=request.user)
        return {'cp_visits':visits}
    else:
        return {}