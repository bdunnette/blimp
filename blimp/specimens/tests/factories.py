import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from blimp.specimens.models import Container
from blimp.specimens.models import ContainerLocation
from blimp.specimens.models import Specimen


class ContainerLocationFactory(DjangoModelFactory):
    class Meta:
        model = ContainerLocation

    name = factory.Sequence(lambda n: f"Location {n}")
    description = factory.Faker("sentence")


class ContainerFactory(DjangoModelFactory):
    class Meta:
        model = Container

    name = factory.Sequence(lambda n: f"Container {n}")
    type = "Box"
    location = factory.SubFactory(ContainerLocationFactory)
    rows = 10
    cols = 10


class SpecimenFactory(DjangoModelFactory):
    class Meta:
        model = Specimen

    specimen_id = factory.Sequence(lambda n: f"SPEC-{n:05d}")
    collection_id = factory.Sequence(lambda n: f"COLL-{n:05d}")
    type = Specimen.SpecimenType.BLOOD
    source_subject = factory.Sequence(lambda n: f"SUBJ-{n:05d}")
    collection_date = factory.LazyFunction(timezone.now)
    volume = 1.0
    unit = "ml"
    container = factory.SubFactory(ContainerFactory)
    row = 1
    column = 1
    status = Specimen.SpecimenStatus.AVAILABLE
    notes = factory.Faker("text")
