from django.contrib import admin
from import_export.admin import ImportExportMixin
from simple_history.admin import SimpleHistoryAdmin

from .models import Container
from .models import ContainerLocation
from .models import Specimen
from .resources import ContainerLocationResource
from .resources import ContainerResource
from .resources import SpecimenResource


@admin.register(ContainerLocation)
class ContainerLocationAdmin(ImportExportMixin, SimpleHistoryAdmin):
    resource_classes = [ContainerLocationResource]
    list_display = ("name", "parent", "description")
    search_fields = ("name", "description")


@admin.register(Container)
class ContainerAdmin(ImportExportMixin, SimpleHistoryAdmin):
    resource_classes = [ContainerResource]
    list_display = ("name", "type", "location", "rows", "cols")
    list_filter = ("type", "location")
    search_fields = ("name", "type")


@admin.register(Specimen)
class SpecimenAdmin(ImportExportMixin, SimpleHistoryAdmin):
    resource_classes = [SpecimenResource]
    list_display = (
        "specimen_id",
        "type",
        "source_subject",
        "collection_date",
        "status",
        "container",
        "row",
        "column",
    )
    list_filter = ("type", "status", "collection_date", "container")
    search_fields = (
        "specimen_id",
        "collection_id",
        "source_subject",
    )
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "collection_date"
