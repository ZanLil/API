from django.contrib import admin

from api.models import PerevalAdded, PerevalAreas, PerevalImages, SprActivitiesTypes


@admin.register(PerevalAdded)
class PerevalAddedAdmin(admin.ModelAdmin):
    pass


@admin.register(PerevalAreas)
class PerevalAreasAdmin(admin.ModelAdmin):
    pass


@admin.register(PerevalImages)
class PerevalImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(SprActivitiesTypes)
class SprActivitiesTypesAdmin(admin.ModelAdmin):
    pass
