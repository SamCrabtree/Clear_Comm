from django import forms
from .models import property, note, Loop, Tent
from ckeditor.fields import RichTextField

class LeadForm(forms.ModelForm):
    class Meta:
        model = property
        fields = ('address', 'city', 'state', 'zip_code', 'property_type', 'contact', 'phone', 'origin')

        widgets = {
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control'}),
            'property_type': forms.Select(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'origin': forms.TextInput(attrs={'class':'form-control'}),

        }

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = property
        fields = ('status', 'contact', 'phone', 'email')

        widgets = {
            'status': forms.Select(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),

        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = note
        fields = ('note_type', 'note' )

        widgets = {
            'note_type': forms.Select(attrs={'class':'form-control'}),
            'note': forms.Textarea(attrs={'class':'form-control'}),

        }
    

class LoopForm(forms.ModelForm):
    class Meta:
        model = Loop
        fields = ('loop', 'loop_type', 'contact', 'goal')

        widgets = {
            'loop': forms.TextInput(attrs={'class':'form-control'}),
            'loop_type': forms.Select(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'goal': forms.TextInput(attrs={'class':'form-control'}),

        }

class UpdateLoopForm(forms.ModelForm):
    class Meta:
        model = Loop
        fields = ('loop', 'loop_type', 'contact', 'goal')

        widgets = {
            'loop': forms.TextInput(attrs={'class':'form-control'}),
            'loop_type': forms.Select(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'goal': forms.TextInput(attrs={'class':'form-control'}),

        }

class TentForm(forms.ModelForm):
    class Meta:
        model = Tent
        fields = ('door', 'key_1', 'key_2', 'key_3', 'key_4', 'lessons')

        widgets = {
            'door': forms.TextInput(attrs={'class':'form-control'}),
            'key_1': forms.TextInput(attrs={'class':'form-control'}),
            'key_2': forms.TextInput(attrs={'class':'form-control'}),
            'key_3': forms.TextInput(attrs={'class':'form-control'}),
            'key_4': forms.TextInput(attrs={'class':'form-control'}),
            'lessons': forms.TextInput(attrs={'class':'form-control'}),

        }

class UpdateTentForm(forms.ModelForm):
    class Meta:
        model = Tent
        fields = ('door', 'key_1', 'key_2', 'key_3', 'key_4', 'lessons')

        widgets = {
            'door': forms.TextInput(attrs={'class':'form-control'}),
            'key_1': forms.TextInput(attrs={'class':'form-control'}),
            'key_2': forms.TextInput(attrs={'class':'form-control'}),
            'key_3': forms.TextInput(attrs={'class':'form-control'}),
            'key_4': forms.TextInput(attrs={'class':'form-control'}),
            'lessons': forms.TextInput(attrs={'class':'form-control'}),


        }