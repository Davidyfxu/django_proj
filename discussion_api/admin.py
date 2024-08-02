from django.contrib import admin

from discussion_api.models import DiscussionData


# Register your models here.
class DiscussionDataAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'topic_id', 'entry_id', 'entry_user_id', 'entry_workflow_state', 'entry_created_at')
    search_fields = ('course_id', 'topic_id', 'entry_id', 'entry_user_id')
    list_filter = ('entry_workflow_state',)


admin.site.register(DiscussionData, DiscussionDataAdmin)
