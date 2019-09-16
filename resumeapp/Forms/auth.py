from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter UserName','name':'UserName'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','placeholder':'Enter Password','name':'Password'}))

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter FirstName','name':'first_name'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter LastName','name':'last_name'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter UserName','name':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter Password','name':'password'}))
