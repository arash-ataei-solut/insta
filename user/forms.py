from django.contrib.auth.forms import UserCreationForm

from user.models import Profile


class RegistrationForm(UserCreationForm):

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=commit)
        Profile.objects.create(user=user)
        return user
