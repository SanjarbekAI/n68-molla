from django.contrib import admin

from apps.pages.models import ContactModel, TeamModel

admin.site.register(ContactModel)

@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display =['id', 'full_name']
    search_fields = ['full_name']
    list_filter = ['created_at']