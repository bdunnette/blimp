import pytest

from blimp.users.tasks import get_users_count
from blimp.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_user_count(settings):
    """A basic test to execute the get_users_count Huey task."""
    batch_size = 3
    UserFactory.create_batch(batch_size)
    # Huey immediate mode is set in base settings for DEBUG,
    # but for tests we can rely on how it's configured.
    # In Huey, .call() executes the function immediately and returns the value.
    # or we can use .delay() and check results if configured.
    # Given the task is a db_task, we just want to see it run.
    assert get_users_count() == batch_size
