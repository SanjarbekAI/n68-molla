from django.contrib import admin

from apps.pages.models import ContactModel, StoreModel

admin.site.register(ContactModel)

@admin.register(StoreModel)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'phone_number', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'location')
    search_fields = ('title', 'location', 'phone_number')
    ordering = ('-id',)