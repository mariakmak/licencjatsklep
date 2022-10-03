from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class Search(forms.Form):
    wyszukaj = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control mr-sm-2',  'placeholder':'Wyszukaj'}))

class LoginAuthForm(AuthenticationForm):


    def __init__(self, *args, **kwargs):
        super(LoginAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'



class Register(UserCreationForm):
    first_name = forms.CharField(required=True, label='Imie', widget=forms.TextInput(attrs={'class':'form-control'}) )
    last_name = forms.CharField(required=True, label='Nazwisko', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    #log_on = forms.BooleanField(label="Logowanie po rejestracji:", required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'





    def save(self, commit=True):
        user = super(Register, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']

        if commit:
            user.save()

        return user






#class Login(AuthenticationForm):
    #username = forms.CharField(required=True, label='Email')

