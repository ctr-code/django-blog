from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title',)
    summernote_fields = ('content',)

    # Prevent multiple instances of About
    def has_add_permission(self, request):
        return not About.objects.exists()
