from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Player

# Register your models here.

admin.site.unregister(User)

class PlayerInline(admin.StackedInline):
    model = Player
    can_delete: bool = False
    verbose_name_plural = "Players"

class PlayerAdmin(UserAdmin):
    inlines = [
        PlayerInline
    ]

admin.site.register(User, PlayerAdmin)
# admin.site.register(Player)