from django import forms
from .models import user,postt

class uform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = user
        fields = ('first_name','last_name','email','username','password')
        
class postform(forms.ModelForm):
    class Meta():
        model = postt
        fields = ('user','text','created_at','updated_at')