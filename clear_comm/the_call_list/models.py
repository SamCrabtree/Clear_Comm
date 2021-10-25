from django.db import models
from django.contrib.auth.models import User



STATUS_CHOICES = (
    ('cold' , 'COLD'),
    ('in contact', 'IN CONTACT'),
    ('appointment set', 'APPOINTMENT SET' ),
    ('offer made' , 'OFFER MADE')
)

NOTE_CHOICES = (
    ('call' , 'CALL'),
    ('text', 'TEXT'),
    ('email', 'EMAIL' ),
    ('internal note' , 'INTERNAL NOTE'),
    ('offer', 'OFFER'),
    ('bad number', 'BAD NUMBER'),
    ('bad email', 'BAD EMAIL'),
    ('do not contact', 'DO NOT CONTACT')
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

class note(models.Model):
    Property = models.ForeignKey(property, related_name='notes', on_delete=models.CASCADE)
    note_type = models.CharField(max_length=500, choices=NOTE_CHOICES, default='internal note')
    note = models.TextField(max_length=1000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.Property.address, self.creator, self.created)