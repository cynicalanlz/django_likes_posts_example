from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):
    email = EmailField(required=True,
                       label='Email',
                       error_messages={'exists': 'Email already exists in db.'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']
