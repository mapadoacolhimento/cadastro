# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MdlUserPreferences(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=1333)

    class Meta:
        managed = False
        db_table = 'mdl_user_preferences'
        unique_together = (('userid', 'name'),)
        db_table_comment = 'Allows modules to store arbitrary user preferences'
