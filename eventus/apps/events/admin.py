from django.contrib import admin

from .models import Category, Event, AssistantEnrolled, Comments

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(AssistantEnrolled)
admin.site.register(Comments)