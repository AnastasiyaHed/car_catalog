from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Car, CarAccessory

class CarAccessoryInline(admin.TabularInline):
    model = CarAccessory
    extra = 1

class CarAdmin(admin.ModelAdmin):
    inlines = [CarAccessoryInline]
    list_display = ('year', 'make', 'model', 'display_image', 'display_link')

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')

    display_image.short_description = 'Image'

    def display_link(self, obj):
        return mark_safe(f'<a href="{obj.link}" target="_blank">{obj.link}</a>')

    display_link.short_description = 'Link'

admin.site.register(Car, CarAdmin)
