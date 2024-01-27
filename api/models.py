from django.db import models


class PerevalAdded(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    raw_data = models.JSONField()
    images = models.JSONField()

    class Meta:
        db_table = 'pereval_added'


class PerevalAreas(models.Model):
    parent = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, related_name='areas')
    title = models.TextField()

    class Meta:
        db_table = 'pereval_areas'


class PerevalImages(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='pereval_images/', blank=True, null=True)

    class Meta:
        db_table = 'pereval_images'


class SprActivitiesTypes(models.Model):
    title = models.TextField()

    class Meta:
        db_table = 'spr_activities_types'
