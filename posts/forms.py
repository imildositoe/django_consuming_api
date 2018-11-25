from django import forms


class Login(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)


class User(forms.Form):
    id_user = forms.CharField(label='id_user', max_length=100)
