from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

TYPE_CHOICES = [
    ('Other' , 'OTHER'),
    ('Single Family' , 'SINGLE FAMILY'),
    ('Commercial', 'COMMERCIAL'),
    ('Duplex', 'DUPLEX' ),
    ('Triplex' , 'TRIPLEX'),
    ('Multiplex', 'MULTIPLEX' ),
    ('Lot/Land', 'LOT/LAND' ),
]

STATUS_CHOICES = [
    ('Cold' , 'COLD'),
    ('In Contact', 'IN CONTACT'),
    ('nurture', 'NURTURE'),
    ('Appointment Set', 'APPOINTMENT SET' ),
    ('Offer Made' , 'OFFER MADE')
]

NOTE_CHOICES = [
    ('Call' , 'CALL'),
    ('Text', 'TEXT'),
    ('Email', 'EMAIL' ),
    ('Internal Note' , 'INTERNAL NOTE'),
    ('Offer', 'OFFER'),
    ('Voicemail', 'VOICEMAIL'),
    ('Bad Number', 'BAD NUMBER'),
    ('Bad Email', 'BAD EMAIL'),
    ('Do Not Contact', 'DO NOT CONTACT')
]


class property(models.Model):
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=12)
    property_type = models.CharField(max_length=500, choices=TYPE_CHOICES, default='Other')
    contact = models.CharField(max_length=500)
    phone = models.CharField(max_length=11)
    origin = models.CharField(max_length=40)
    email = models.EmailField(max_length=99)
    status = models.CharField(max_length=500, choices=STATUS_CHOICES, default='Cold')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('lead', args=(str(self.id))) 

class note(models.Model):
    Property = models.ForeignKey(property, related_name="notes",on_delete=models.CASCADE)
    note_type = models.CharField(max_length=500, choices=NOTE_CHOICES, default='Internal Note')
    note = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.Property, self.creator, self.note_type, self.note, self.created)
