from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Dataset, TestCase
from .forms import UserCreationForm, UserChangeForm

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

class TestCaseInline(admin.StackedInline):
    model = TestCase
    extra = 3

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    inlines = [ TestCaseInline ]
