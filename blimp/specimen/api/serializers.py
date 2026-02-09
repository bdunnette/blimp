from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from blimp.specimen.models import Study, StudyParticipant, StorageLocation, Biospecimen


class StudySerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Study
        fields = ["id", "name", "code", "description", "tags", "created", "modified"]


class StudyParticipantSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = StudyParticipant
        fields = ["id", "study", "external_id", "enrollment_date", "tags", "created", "modified"]


class StorageLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageLocation
        fields = ["id", "name", "parent", "description", "created", "modified"]


class BiospecimenSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Biospecimen
        fields = [
            "id",
            "participant",
            "collection_date",
            "type",
            "volume",
            "volume_unit",
            "storage_location",
            "status",
            "metadata",
            "tags",
            "created",
            "modified",
        ]
