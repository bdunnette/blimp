from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from taggit.managers import TaggableManager


class Study(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=255)
    code = models.CharField(_("Code"), max_length=50, unique=True)
    description = models.TextField(_("Description"), blank=True)

    history = HistoricalRecords()
    tags = TaggableManager()

    class Meta:
        verbose_name = _("Study")
        verbose_name_plural = _("Studies")

    def __str__(self):
        return f"{self.name} ({self.code})"


class StudyParticipant(TimeStampedModel):
    study = models.ForeignKey(Study, on_delete=models.CASCADE, related_name="participants")
    external_id = models.CharField(_("External ID"), max_length=100)
    enrollment_date = models.DateField(_("Enrollment Date"), null=True, blank=True)

    history = HistoricalRecords()
    tags = TaggableManager()

    class Meta:
        unique_together = ("study", "external_id")
        verbose_name = _("Study Participant")
        verbose_name_plural = _("Study Participants")

    def __str__(self):
        return f"{self.external_id} ({self.study.code})"


class StorageLocation(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )
    description = models.TextField(_("Description"), blank=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("Storage Location")
        verbose_name_plural = _("Storage Locations")

    def __str__(self):
        if self.parent:
            return f"{self.parent} -> {self.name}"
        return self.name


class Biospecimen(TimeStampedModel):
    SPECIMEN_TYPES = [
        ("blood", _("Blood")),
        ("urine", _("Urine")),
        ("saliva", _("Saliva")),
        ("tissue", _("Tissue")),
        ("other", _("Other")),
    ]

    participant = models.ForeignKey(
        StudyParticipant,
        on_delete=models.CASCADE,
        related_name="specimens",
    )
    collection_date = models.DateTimeField(_("Collection Date"))
    type = models.CharField(_("Type"), max_length=50, choices=SPECIMEN_TYPES)
    volume = models.DecimalField(_("Volume"), max_digits=10, decimal_places=2, null=True, blank=True)
    volume_unit = models.CharField(_("Volume Unit"), max_length=20, blank=True)
    storage_location = models.ForeignKey(
        StorageLocation,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="specimens",
    )
    status = models.CharField(_("Status"), max_length=50, default="stored")

    history = HistoricalRecords()
    tags = TaggableManager()

    class Meta:
        verbose_name = _("Biospecimen")
        verbose_name_plural = _("Biospecimens")

    def __str__(self):
        return f"{self.type} - {self.participant.external_id} ({self.collection_date.date()})"
