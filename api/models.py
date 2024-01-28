from django.db import models


class PerevalAdded(models.Model):
    """Модель с перевалами."""

    class Status(models.TextChoices):
        """Вариации для поля status."""
        NEW = 'new', 'new'
        PENDING = 'pending', 'pending'
        ACCEPTED = 'accepted', 'accepted'
        REJECTED = 'rejected', 'rejected'

    date_added = models.DateTimeField(auto_now_add=True)
    raw_data = models.JSONField()
    images = models.JSONField()
    status = models.CharField(max_length=8, choices=Status.choices, default=Status.NEW)
    user_email = models.EmailField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'pereval_added'


class PerevalAreas(models.Model):
    """Модель области."""
    parent = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, related_name='areas')
    title = models.TextField()

    class Meta:
        db_table = 'pereval_areas'


class PerevalImages(models.Model):
    """Модель с изображением."""
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='pereval_images/', blank=True, null=True)

    class Meta:
        db_table = 'pereval_images'


class SprActivitiesTypes(models.Model):
    """Модель видов деятельности."""
    title = models.TextField()

    class Meta:
        db_table = 'spr_activities_types'
