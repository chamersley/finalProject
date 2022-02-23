from django.contrib import admin
from account.models import createAccount
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class AccountInLine(admin.StackedInline):
    model = createAccount
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInLine, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
