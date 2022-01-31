from django.contrib import admin
from .models import Client, Comment, Vehicle


# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle


admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(Vehicle)
