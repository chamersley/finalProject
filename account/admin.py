from django.contrib import admin
from account.models import createAccount
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

class AccountInLine(admin.StackedInline):
    model = createAccount
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInLine, )


admin.site.register(User, CustomizedUserAdmin)
#admin.site.unregister(get_user_model())

admin.site.register(createAccount)

