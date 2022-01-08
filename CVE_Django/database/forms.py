from django import forms
 
class UserForm(forms.Form):
    order = forms.CharField(help_text='only "question_text" or "-question_text" available', required=False)