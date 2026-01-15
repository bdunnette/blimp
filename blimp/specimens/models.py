from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class Specimen(models.Model):
    class SpecimenType(models.TextChoices):
        BLOOD = "BLOOD", _("Blood")
        SERUM = "SERUM", _("Serum")
        PLASMA = "PLASMA", _("Plasma")
        DNA = "DNA", _("DNA")
        RNA = "RNA", _("RNA")
        TISSUE = "TISSUE", _("Tissue")
        URINE = "URINE", _("Urine")
        OTHER = "OTHER", _("Other")

    class SpecimenStatus(models.TextChoices):
        AVAILABLE = "AVAILABLE", _("Available")
        DEPLETED = "DEPLETED", _("Depleted")
        RESERVED = "RESERVED", _("Reserved")
        DESTROYED = "DESTROYED", _("Destroyed")

    specimen_id = models.CharField(_("Specimen ID"), max_length=100, unique=True)
    collection_id = models.CharField(_("Collection ID"), max_length=100, blank=True)
    type = models.CharField(
        _("Type"),
        max_length=20,
        choices=SpecimenType.choices,
        default=SpecimenType.OTHER,
    )
    source_subject = models.CharField(_("Source Subject"), max_length=100)
    collection_date = models.DateTimeField(_("Collection Date"), null=True, blank=True)
    volume = models.DecimalField(
        _("Volume"),
        max_digits=10,
        decimal_places=3,
        null=True,
        blank=True,
    )
    unit = models.CharField(_("Unit"), max_length=20, blank=True)
    storage_location = models.CharField(
        _("Storage Location"),
        max_length=255,
        blank=True,
    )
    status = models.CharField(
        _("Status"),
        max_length=20,
        choices=SpecimenStatus.choices,
        default=SpecimenStatus.AVAILABLE,
    )
    notes = models.TextField(_("Notes"), blank=True)

    history = HistoricalRecords()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Specimen")
        verbose_name_plural = _("Specimens")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.specimen_id} ({self.get_type_display()})"
