from django import forms

class ContactForm(forms.Form):
    

    encryption_type = forms.ChoiceField(choices= [('',''),('caesar','Casesar Cipher'),('transposition','Transposition Cipher')],label = 'Encryption')

   
    key  = forms.IntegerField(label = 'Key')

    string = forms.CharField(label ='Input String',widget = forms.Textarea)

    mode = forms.ChoiceField(choices = [('enc','Encryption'),('dec','Decryption')], widget = forms.RadioSelect, label = 'Mode')

