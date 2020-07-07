from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserEditForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email",)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("dob", "profile_picture",)


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)


    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email",)

    def clean_password2(self):
        clean_data = self.cleaned_data
        if clean_data["password"] != clean_data["password2"]:
            raise forms.ValidationError("Passwords don't match.")

        return clean_data["password2"]