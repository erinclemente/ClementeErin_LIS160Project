from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

# this is for the registration
class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'	
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'	
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal info.</li><li>Your password needs to be at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'	
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Re-enter the password for confirmation.</small></span>'

# this adds a record form for a DreamDoc
# See Note in models.py for the context of the comments below

class AddRecordForm(forms.ModelForm):
	# first_name -> title
	first_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Dream Title  -  because all stories must have a name !", "class":"form-control"}), label="")
	# last_name -> author
	last_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Author  -  that's you !", "class":"form-control"}), label="")
	# email -> dream_type
	email = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Dream Type  -  vivid / lucid / nightmare / recurring / etc", "class":"form-control"}), label="")
	# phone -> dreamed_at
	phone = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Dreamed At  -  when? where?", "class":"form-control"}), label="")
	# address -> dream_content
	address = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Dream Content  -  tell us all about it !", "class":"form-control"}), label="")
	# city -> emotions_felt
	city = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Emotions Felt  -  can be during or after the dream", "class":"form-control"}), label="")
	# state -> poss_causes
	state = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Possible Causes  -  what factors in your life might've contributed?", "class":"form-control"}), label="")
	# zipcode -> takeaways
	zipcode = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Analysis & Takeaways  -  what can you learn from this?", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)
