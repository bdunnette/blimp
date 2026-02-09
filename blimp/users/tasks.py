from huey.contrib.djhuey import db_task

from .models import User


@db_task()
def get_users_count():
    """A pointless Huey task to demonstrate usage."""
    return User.objects.count()
