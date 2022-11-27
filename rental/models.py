from django.db import models


# Create your models here.
from django.urls import reverse


class Rental(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rent = models.ForeignKey(Rental, on_delete=models.CASCADE)
    rental_id = models.CharField(max_length=100)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"{self.checkin} - {self.checkout}"

    class Meta:
        ordering = ['rental_id']
        constraints = [
            models.CheckConstraint(
                check=(models.Q(checkin__lte=models.F('checkout'))
                       ),
                name='checkin_lte_checkout'
            ),
        ]
