from django import forms
from .models import GuestBookPost

class GuestBookForm(forms.ModelForm):
	class Meta:
		model = GuestBookPost
		fields = ('author','text',)
		widgets = {
			'text': forms.Textarea(attrs={'rows':5}),
		}