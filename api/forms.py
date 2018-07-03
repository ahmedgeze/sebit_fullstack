from django import forms

# class postForm(forms.Form):
#      id = forms.CharField(label='Enter your id', max_length=100)
#      name = forms.CharField(label='Enter your name', max_length=100)
#      city = forms.CharField(label='Enter your city', max_length=100)
#      country = forms.CharField(label='Enter your country', max_length=100)

class personForm(forms.Form):
     name = forms.CharField(label='Enter your name', max_length=100)
     city = forms.CharField(label='Enter your city', max_length=100)
     country = forms.CharField(label='Enter your country', max_length=100)

class queryForm(forms.Form):
     city = forms.CharField(required=False,label='Enter your city', max_length=100)
     country = forms.CharField(required=False,label='Enter your country', max_length=100)
