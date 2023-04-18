from django.contrib import admin
from exerimets.models import Group, Person, Images


class ImagesInline(admin.TabularInline):
    model = Images.person.through


class MembershipInline(admin.TabularInline):
    model = Group.members.through


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
        ImagesInline,
    ]

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ["members"]