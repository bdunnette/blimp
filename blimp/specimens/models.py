from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class ContainerLocation(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("Parent Location"),
    )
    description = models.TextField(_("Description"), blank=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("Container Location")
        verbose_name_plural = _("Container Locations")

    def __str__(self):
        if self.parent:
            return f"{self.parent} > {self.name}"
        return self.name


class Container(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    type = models.CharField(_("Type"), max_length=50, blank=True)
    location = models.ForeignKey(
        ContainerLocation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="containers",
        verbose_name=_("Location"),
    )
    rows = models.PositiveIntegerField(_("Rows"), default=1)
    cols = models.PositiveIntegerField(_("Columns"), default=1)

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("Container")
        verbose_name_plural = _("Containers")

    def __str__(self):
        return self.name


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
    parent_specimen = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="aliquots",
        verbose_name=_("Parent Specimen"),
    )
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
    container = models.ForeignKey(
        Container,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="specimens",
        verbose_name=_("Container"),
    )
    row = models.PositiveIntegerField(_("Row"), null=True, blank=True)
    column = models.PositiveIntegerField(_("Column"), null=True, blank=True)
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
