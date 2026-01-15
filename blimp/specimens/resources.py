from import_export import resources

from .models import Container
from .models import ContainerLocation
from .models import Specimen


class ContainerLocationResource(resources.ModelResource):
    class Meta:
        model = ContainerLocation
        fields = ("id", "name", "parent", "description")


class ContainerResource(resources.ModelResource):
    class Meta:
        model = Container
        fields = ("id", "name", "type", "location", "rows", "cols")


class SpecimenResource(resources.ModelResource):
    class Meta:
        model = Specimen
        import_id_fields = ("specimen_id",)
        fields = (
            "specimen_id",
            "parent_specimen",
            "collection_id",
            "type",
            "source_subject",
            "collection_date",
            "volume",
            "unit",
            "container",
            "row",
            "column",
            "status",
            "notes",
        )
