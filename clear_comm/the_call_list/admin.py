from django.contrib import admin
from .models import property, note, Loop, Tent

# Register your models here.
admin.site.register(property)
admin.site.register(note)
admin.site.register(Loop)
admin.site.register(Tent)