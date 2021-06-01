import pytest
<<<<<<< HEAD
from django.conf import settings
=======
>>>>>>> with-stripe-connect
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
<<<<<<< HEAD
from django.http import HttpRequest
from django.test import RequestFactory
from django.urls import reverse
=======
from django.http.response import Http404
from django.test import RequestFactory
>>>>>>> with-stripe-connect

from djgumroad.users.forms import UserChangeForm
from djgumroad.users.models import User
from djgumroad.users.tests.factories import UserFactory
from djgumroad.users.views import (
    UserRedirectView,
    UserUpdateView,
    user_detail_view,
)

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

<<<<<<< HEAD
    def dummy_get_response(self, request: HttpRequest):
        return None

=======
>>>>>>> with-stripe-connect
    def test_get_success_url(self, user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(self, user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user

    def test_form_valid(self, user: User, rf: RequestFactory):
        view = UserUpdateView()
        request = rf.get("/fake-url/")

        # Add the session/message middleware to the request
<<<<<<< HEAD
        SessionMiddleware(self.dummy_get_response).process_request(request)
        MessageMiddleware(self.dummy_get_response).process_request(request)
=======
        SessionMiddleware().process_request(request)
        MessageMiddleware().process_request(request)
>>>>>>> with-stripe-connect
        request.user = user

        view.request = request

        # Initialize the form
        form = UserChangeForm()
        form.cleaned_data = []
        view.form_valid(form)

        messages_sent = [m.message for m in messages.get_messages(request)]
        assert messages_sent == ["Information successfully updated"]


class TestUserRedirectView:
    def test_get_redirect_url(self, user: User, rf: RequestFactory):
        view = UserRedirectView()
        request = rf.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestUserDetailView:
    def test_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = UserFactory()

        response = user_detail_view(request, username=user.username)

        assert response.status_code == 200

    def test_not_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = AnonymousUser()

        response = user_detail_view(request, username=user.username)
<<<<<<< HEAD
        login_url = reverse(settings.LOGIN_URL)

        assert response.status_code == 302
        assert response.url == f"{login_url}?next=/fake-url/"
=======

        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=/fake-url/"

    def test_case_sensitivity(self, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = UserFactory(username="UserName")

        with pytest.raises(Http404):
            user_detail_view(request, username="username")
>>>>>>> with-stripe-connect
