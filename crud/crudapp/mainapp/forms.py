from .models import User
from django import forms
class Register(forms.ModelForm):
    class Meta():
        model=User
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True ,attrs={'class':'form-control'}),
            
        }
     