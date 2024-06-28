# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Content(models.Model):
    title = models.CharField(db_column='Title', primary_key=True, max_length=50)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=25, blank=True, null=True)  # Field name made lowercase.
    release_date = models.DateField(db_column='Release_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Content'

