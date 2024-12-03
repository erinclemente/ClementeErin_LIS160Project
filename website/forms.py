from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_Length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_Length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		field = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def__init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'	
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only</small></span>'

		self.fields['username'].widget.attrs['class'] = 'form-control'	
		self.fields['username'].widget.attrs['placeholder'] = 'Password'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal info.</li><li>Your password needs to be at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['username'].widget.attrs['class'] = 'form-control'	
		self.fields['username'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Re-enter the password for confirmation.</small></span>'