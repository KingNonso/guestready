from django.http import HttpResponse
from django.template import loader

from .models import Reservation


def index(request):
    reservations = Reservation.objects.all()
    template = loader.get_template('rental/index.html')
    context = {
        'reservations': reservations,
    }
    return HttpResponse(template.render(context, request))
