<<<<<<< HEAD
"""
Module for all Form Tests.
"""
import pytest
from django.utils.translation import ugettext_lazy as _

from djgumroad.users.forms import UserCreationForm
from djgumroad.users.models import User
=======
import pytest

from djgumroad.users.forms import UserCreationForm
from djgumroad.users.tests.factories import UserFactory
>>>>>>> with-stripe-connect

pytestmark = pytest.mark.django_db


class TestUserCreationForm:
<<<<<<< HEAD
    """
    Test class for all tests related to the UserCreationForm
    """

    def test_username_validation_error_msg(self, user: User):
        """
        Tests UserCreation Form's unique validator functions correctly by testing:
            1) A new user with an existing username cannot be added.
            2) Only 1 error is raised by the UserCreation Form
            3) The desired error message is raised
        """

        # The user already exists,
        # hence cannot be created.
        form = UserCreationForm(
            {
                "username": user.username,
                "password1": user.password,
                "password2": user.password,
=======
    def test_clean_username(self):
        # A user with proto_user params does not exist yet.
        proto_user = UserFactory.build()

        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user._password,
                "password2": proto_user._password,
            }
        )

        assert form.is_valid()
        assert form.clean_username() == proto_user.username

        # Creating a user.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user._password,
                "password2": proto_user._password,
>>>>>>> with-stripe-connect
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors
<<<<<<< HEAD
        assert form.errors["username"][0] == _("This username has already been taken.")
=======
>>>>>>> with-stripe-connect
