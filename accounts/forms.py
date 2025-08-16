from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        """
        Getting last_name,email,is_writer and first_name from the customuser
        """
        fields = ["first_name", "last_name", "email", "is_writer", "password1", "password2"]
        # password1 and password2 come with UserCreationForm by default

    # Ensure email is unique
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email
