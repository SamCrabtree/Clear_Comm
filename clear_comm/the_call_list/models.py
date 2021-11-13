from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField 

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
    ('Nurture', 'NURTURE'),
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

LOOP_CHOICES = [
    ('Financial' , 'FINANCIAL'),
    ('Note Follow Up', 'NOTE FOLLOW UP'),
    ('Legal Follow Up', 'LEGAL FOLLOW UP' ),
    ('Investor Follow Up' , 'INVESTOR FOLLOW UP'),
    ('Oppurtunities', 'OPPURTUNITIES')
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
    note = RichTextField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.Property, self.creator, self.note_type, self.note, self.created)

class Tent(models.Model):
    door = models.TextField(max_length=250)
    key_1 = models.TextField(max_length=250)
    key_2 = models.TextField(max_length=250)
    key_3 = models.TextField(max_length=250)
    key_4 = models.TextField(max_length=250)
    lessons = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)

   
class Loop (models.Model):
    loop = models.TextField(max_length=500)
    loop_type = models.CharField(max_length=500, choices=LOOP_CHOICES, default='Other')
    contact = models.TextField(max_length=200)
    goal = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.loop



