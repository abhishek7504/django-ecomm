from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):


    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number','email','first_name','last_name')

    def cleaned_data(self):
        qs = self.cleaned_data.get('phone_number')
        if qs.exists() and qs.count() == 1:
            raise forms.ValidationError('This phone number already exists')
        return qs    
        
    def clean_password2(self):

        cd = self.cleaned_data
        if cd['password'] != cd['password2'] :
            raise forms.ValidationError('PASSWORD DOESN\'T MATCH')

        return cd['password']  


class LoginForm(forms.Form):
    username = forms.CharField(label="Email or Phone number")
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
