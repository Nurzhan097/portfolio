from django import forms
from . import models


class ContactForm(forms.ModelForm):
	class Meta:
		model = models.Contact
		fields = [
			'name',
			'email',
			'phone',
			'desired_contact_method',
			'products',
			'message',
		]

		widgets = {
			'name': forms.TextInput(attrs={'class': 'md-input style-02 ', 'placeholder': "Name", }),
			'email': forms.TextInput(attrs={'class': 'md-input style-02', 'placeholder': "E-mail", }),
			'phone': forms.TextInput(attrs={'class': 'md-input style-02', 'placeholder': "Phone", }),
			'desired_contact_method': forms.Select(attrs={'class': 'md-input style-02', 'placeholder': "Желаемый способ контакта", }),
			'products': forms.Select(attrs={'class': 'md-input style-02', 'placeholder': "Products",  'size': '10'}),
			'message': forms.Textarea(attrs={'class': 'md-input style-02', 'placeholder': "Комментарий", }),
		}





