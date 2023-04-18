from django.contrib import admin
from exerimets.models import Group, Person


class MembershipInline(admin.TabularInline):
    model = Group.members.through


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ["members"]