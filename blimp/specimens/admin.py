from django.contrib import admin
from import_export.admin import ImportExportMixin
from simple_history.admin import SimpleHistoryAdmin

from .models import Specimen
from .resources import SpecimenResource


@admin.register(Specimen)
class SpecimenAdmin(ImportExportMixin, SimpleHistoryAdmin):
    resource_classes = [SpecimenResource]
    list_display = (
        "specimen_id",
        "type",
        "source_subject",
        "collection_date",
        "status",
        "volume",
        "unit",
    )
    list_filter = ("type", "status", "collection_date")
    search_fields = (
        "specimen_id",
        "collection_id",
        "source_subject",
        "storage_location",
    )
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "collection_date"
