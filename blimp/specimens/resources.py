from import_export import resources

from .models import Specimen


class SpecimenResource(resources.ModelResource):
    class Meta:
        model = Specimen
        import_id_fields = ("specimen_id",)
        fields = (
            "specimen_id",
            "collection_id",
            "type",
            "source_subject",
            "collection_date",
            "volume",
            "unit",
            "storage_location",
            "status",
            "notes",
        )
