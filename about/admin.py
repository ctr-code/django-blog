from django.contrib import admin
from .models import About, CollaborationRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title',)
    summernote_fields = ('content',)

    # Prevent multiple instances of About
    def has_add_permission(self, request):
        return not About.objects.exists()


# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

@admin.register(CollaborationRequest)
class CollaborationRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
