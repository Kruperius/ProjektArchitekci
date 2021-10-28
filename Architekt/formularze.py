from django import forms
from .models import Projekt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# class Dodaj_arch(forms.ModelForm):
# 	email = forms.EmailField(max_length=200, help_text='Required')
# 	class Meta:
# 		model = Architekt
# 		fields = ['imie', 'nazwisko', 'data_ur', 'adres', 'adres2', 'nr_tel', 'nr_tel2', 'email', 'projekty']

class SignUpForm(UserCreationForm):
	imie=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	nazwisko=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	username=forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
	data_ur=forms.DateField(label='Data ur.', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
	# adres=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	# adres2=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	# nr_tel=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	# nr_tel2=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	# projekty=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
	password1=forms.CharField(label='Hasło', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	password2=forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

	class Meta:
		model = get_user_model()
		fields = ['imie', 'nazwisko', 'username', 'data_ur', 'email', 'password1', 'password2']
		# fields = ['first_name', 'last_name', 'email', 'username']
		# fields = ['imie', 'nazwisko', 'data_ur', 'adres', 'adres2', 'nr_tel', 'nr_tel2', 'email', 'projekty']

class Dodaj_proj(forms.ModelForm):
	# UserModel = get_user_model()
	# architekt = forms.ModelChoiceField(queryset=UserModel.objects.all(), disabled=True)
	nazwa=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	grafika=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}))
	rok_powstania=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Projekt
		fields = ['nazwa', 'grafika', 'rok_powstania']
	# def save(self, **kwargs):
	# 	user = kwargs.pop('user')
	# 	instance = super(CategoryNameForm, self).save(**kwargs)
	# 	instance.user = user
	# 	instance.save()
	# 	return instance