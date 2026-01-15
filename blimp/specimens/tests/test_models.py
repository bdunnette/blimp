import pytest
from django.db import IntegrityError

from blimp.specimens.models import Specimen
from blimp.specimens.tests.factories import ContainerFactory
from blimp.specimens.tests.factories import ContainerLocationFactory
from blimp.specimens.tests.factories import SpecimenFactory

pytestmark = pytest.mark.django_db


def test_container_location_str():
    location = ContainerLocationFactory(name="Room 101")
    assert str(location) == "Room 101"

    sub_location = ContainerLocationFactory(name="Fridge A", parent=location)
    assert str(sub_location) == "Room 101 > Fridge A"


def test_container_str():
    container = ContainerFactory(name="Box 1")
    assert str(container) == "Box 1"


def test_specimen_str():
    specimen = SpecimenFactory(specimen_id="S-123", type=Specimen.SpecimenType.BLOOD)
    assert str(specimen) == "S-123 (Blood)"


def test_specimen_unique_id():
    SpecimenFactory(specimen_id="DUPE")
    with pytest.raises(IntegrityError):
        SpecimenFactory(specimen_id="DUPE")


def test_specimen_aliquot_relationship():
    parent = SpecimenFactory(specimen_id="PARENT")
    child = SpecimenFactory(specimen_id="CHILD", parent_specimen=parent)

    assert child.parent_specimen == parent
    assert parent.aliquots.count() == 1
    assert parent.aliquots.first() == child


def test_specimen_container_relationship():
    container = ContainerFactory(name="The Box")
    specimen = SpecimenFactory(container=container)

    assert specimen.container == container
    assert container.specimens.count() == 1
    assert container.specimens.first() == specimen
