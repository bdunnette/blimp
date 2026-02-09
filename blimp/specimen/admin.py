from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from .models import Study, StudyParticipant, StorageLocation, Biospecimen


@admin.register(Study)
class StudyAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ("name", "code", "created")
    search_fields = ("name", "code")


@admin.register(StudyParticipant)
class StudyParticipantAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ("external_id", "study", "enrollment_date")
    list_filter = ("study",)
    search_fields = ("external_id",)


@admin.register(StorageLocation)
class StorageLocationAdmin(SimpleHistoryAdmin):
    list_display = ("name", "parent")
    search_fields = ("name",)


@admin.register(Biospecimen)
class BiospecimenAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ("participant", "type", "collection_date", "storage_location", "status")
    list_filter = ("type", "status", "participant__study")
    search_fields = ("participant__external_id", "tags__name")
    raw_id_fields = ("participant", "storage_location")
