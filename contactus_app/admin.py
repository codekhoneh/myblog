from django.contrib import admin
from .models import footer, ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'birth_year', 'created_at')
	list_filter = ('birth_year', 'created_at')
	search_fields = ('name', 'email', 'text')


admin.site.register(footer)
