from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from blimp.specimen.models import Study, StudyParticipant, StorageLocation, Biospecimen
from .serializers import (
    StudySerializer,
    StudyParticipantSerializer,
    StorageLocationSerializer,
    BiospecimenSerializer,
)


class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class StudyParticipantViewSet(viewsets.ModelViewSet):
    queryset = StudyParticipant.objects.all()
    serializer_class = StudyParticipantSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class StorageLocationViewSet(viewsets.ModelViewSet):
    queryset = StorageLocation.objects.all()
    serializer_class = StorageLocationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class BiospecimenViewSet(viewsets.ModelViewSet):
    queryset = Biospecimen.objects.all()
    serializer_class = BiospecimenSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
