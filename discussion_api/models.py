from django.db import models


class DiscussionData(models.Model):
    course_id = models.BigIntegerField(blank=True, null=True)
    course_code = models.TextField(blank=True, null=True)
    course_name = models.TextField(blank=True, null=True)
    course_created_at = models.TextField(blank=True, null=True)
    course_updated_at = models.TextField(blank=True, null=True)
    course_workflow_state = models.TextField(blank=True, null=True)
    topic_id = models.FloatField(blank=True, null=True)
    topic_title = models.TextField(blank=True, null=True)
    topic_content = models.TextField(blank=True, null=True)
    topic_user_id = models.FloatField(blank=True, null=True)
    topic_deleted_at = models.TextField(blank=True, null=True)
    topic_created_at = models.TextField(blank=True, null=True)
    topic_updated_at = models.TextField(blank=True, null=True)
    topic_workflow_state = models.TextField(blank=True, null=True)
    topic_lock_at = models.TextField(blank=True, null=True)
    topic_posted_at = models.TextField(blank=True, null=True)
    entry_id = models.FloatField(blank=True, null=True)
    entry_content = models.TextField(blank=True, null=True)
    entry_deleted_at = models.TextField(blank=True, null=True)
    entry_user_id = models.FloatField(blank=True, null=True)
    entry_created_at = models.TextField(blank=True, null=True)
    entry_updated_at = models.TextField(blank=True, null=True)
    entry_workflow_state = models.TextField(blank=True, null=True)
    entry_topic_id = models.FloatField(blank=True, null=True)
    entry_parent_id = models.TextField(blank=True, null=True)
    entry_editor_id = models.FloatField(blank=True, null=True)
    entry_root_entry_id = models.TextField(blank=True, null=True)
    entry_depth = models.FloatField(blank=True, null=True)
    entry_rating_count = models.TextField(blank=True, null=True)
    entry_rating_sum = models.TextField(blank=True, null=True)
    parent_entry_user_id = models.TextField(blank=True, null=True)
    topic_user_name = models.TextField(blank=True, null=True)
    entry_user_name = models.TextField(blank=True, null=True)
    parent_entry_user_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_data'
