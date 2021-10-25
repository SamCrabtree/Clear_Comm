from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ('cold' , 'COLD'),
    ('in contact', 'IN CONTACT'),
    ('appointment set', 'APPOINTMENT SET' ),
    ('offer made' , 'OFFER MADE')
)


class property(models.Model):
    address = models.CharField(max_length=500)
    contact = models.CharField(max_length=500)
    phone = models.CharField(max_length=11)
    origin = models.CharField(max_length=40)
    email = models.EmailField(max_length=99)
    status = models.CharField(max_length=500, choices=STATUS_CHOICES, default='cold')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    notes = {}

    def __str__(self):
        return self.address + ' | ' + self.status
