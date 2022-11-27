from django import template

register = template.Library()


@register.filter
def parent(value):
    """Gets the the parent of a reservation.
    The reservation prior to the current reservation of the same rental"""
    parent = value.rent.reservation_set.filter(checkout__lte=value.checkin).order_by('-checkout').first()
    return parent.rental_id if parent else '-'
