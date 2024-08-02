from django.contrib import admin

from read_api.models import ReadData


class ReadDataAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_code', 'course_workflow_state', 'topic_id', 'topic_title', 'topic_user_id',
                    'topic_workflow_state', 'entry_id', 'entry_user_id', 'entry_workflow_state', 'entry_read_user_id',
                    'entry_read_workflow_state', 'entry_created_at')
    search_fields = ('course_id', 'topic_id', 'entry_id', 'entry_user_id')
    list_filter = ('course_workflow_state', 'entry_workflow_state', 'topic_workflow_state')


admin.site.register(ReadData, ReadDataAdmin)
