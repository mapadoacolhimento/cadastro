# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime


class Activists(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=100)
    document_number = models.CharField(blank=True, null=True, max_length=100)
    document_type = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    city = models.CharField(blank=True, null=True, max_length=100)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "activists"


class FormEntries(models.Model):
    widget_id = models.IntegerField(blank=True, null=True)
    fields = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    synchronized = models.BooleanField(blank=True, null=True)
    activist = models.ForeignKey("Activists", models.DO_NOTHING, blank=True, null=True)
    mailchimp_syncronization_at = models.DateTimeField(blank=True, null=True)
    mailchimp_syncronization_error_reason = models.TextField(blank=True, null=True)
    cached_community_id = models.IntegerField()
    rede_syncronized = models.BooleanField(blank=True, null=True)
    mobilization_id = models.IntegerField(blank=True, null=True)
    mailchimp_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "form_entries"
