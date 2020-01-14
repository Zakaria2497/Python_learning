from django import forms

class contactform1(forms.Form):

    
    name = forms.CharField()
    email = forms.EmailField(label = 'E-Mail')
    category = forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)