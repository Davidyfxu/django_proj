from django.db import models


class ReadData(models.Model):
    course_id = models.BigIntegerField(blank=True, null=True)
    course_code = models.TextField(blank=True, null=True)
    course_workflow_state = models.TextField(blank=True, null=True)
    topic_id = models.FloatField(blank=True, null=True)
    topic_title = models.TextField(blank=True, null=True)
    topic_user_id = models.FloatField(blank=True, null=True)
    topic_workflow_state = models.TextField(blank=True, null=True)
    entry_id = models.FloatField(blank=True, null=True)
    entry_user_id = models.FloatField(blank=True, null=True)
    entry_workflow_state = models.TextField(blank=True, null=True)
    entry_read_user_id = models.FloatField(blank=True, null=True)
    entry_read_workflow_state = models.TextField(blank=True, null=True)
    entry_created_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'read_data'
