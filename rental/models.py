from django.db import models


# Create your models here.
from django.urls import reverse


class Rental(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"{self.checkin} - {self.checkout}"

    # def get_absolute_url(self):
    #     return reverse('reservation-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['checkin']
