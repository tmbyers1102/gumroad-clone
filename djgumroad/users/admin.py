from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
<<<<<<< HEAD

=======
from .models import UserLibrary
>>>>>>> with-stripe-connect
from djgumroad.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

<<<<<<< HEAD

=======
admin.site.register(UserLibrary)
>>>>>>> with-stripe-connect
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
<<<<<<< HEAD
<<<<<<< HEAD
        (_("Personal info"), {"fields": ("name", "email")}),
=======
        (_("Personal info"), {"fields": (
            "name",
            "email",
            "stripe_customer_id",
            "stripe_account_id"
            )}),
>>>>>>> with-stripe-connect
=======
        (_("Personal info"), {"fields": ("name", "email", "stripe_customer_id")}),
>>>>>>> with-stripe-connect
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
<<<<<<< HEAD
<<<<<<< HEAD
    list_display = ["username", "name", "is_superuser"]
=======
    list_display = ["username", "name", "stripe_customer_id", "stripe_account_id", "is_superuser"]
>>>>>>> with-stripe-connect
=======
    list_display = ["username", "name", "stripe_customer_id", "is_superuser"]
>>>>>>> with-stripe-connect
    search_fields = ["name"]
