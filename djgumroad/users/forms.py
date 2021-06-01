from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
<<<<<<< HEAD
=======
from django.core.exceptions import ValidationError
>>>>>>> with-stripe-connect
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
<<<<<<< HEAD
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }
=======

    error_message = admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])
>>>>>>> with-stripe-connect
