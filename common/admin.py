from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Dataset
from .forms import UserCreationForm, UserChangeForm

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    pass

#admin.site.register(User, CustomUserAdmin)
