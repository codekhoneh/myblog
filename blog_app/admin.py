from django.contrib import admin
from .models import artikle,category,Comment,ContactMessage
admin.site.register(artikle)
admin.site.register(category)
admin.site.register(Comment)
admin.site.register(ContactMessage) 

# Register your models here.
