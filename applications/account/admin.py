from django.contrib import admin
from django.contrib.auth import get_user_model


# Register your models here.
from applications.account.models import CustomUser

admin.site.register(CustomUser)