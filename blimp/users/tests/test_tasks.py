import pytest

from blimp.users.tasks import get_users_count
from blimp.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_user_count(settings):
    """A basic test to execute the get_users_count task."""
    batch_size = 3
    UserFactory.create_batch(batch_size)
    settings.HUEY.immediate = True
    task_result = get_users_count()
    assert task_result == batch_size
