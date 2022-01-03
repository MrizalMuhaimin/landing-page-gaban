from django import forms

class LoginForm(forms.Form):
    email_field = forms.EmailField(
        widget=forms.EmailInput(
        attrs={
          'id':'lemail',
          'name':'lemail',
          'placeholder':'Email',
        }
      ),
      label="Email address")

    password_field = forms.CharField(
        widget=forms.TextInput(
        attrs={
          'id':'lpassword',
          'name':'lpassword',
          'placeholder':'Password',
          'type':'password'
        }
      ),
      label="Password")
    
    check_field = forms.BooleanField(
        widget=forms.CheckboxInput(
        attrs={
          'id':'keeplogin',
          'name':'keeplogin',
        }
      ),
      )
    


