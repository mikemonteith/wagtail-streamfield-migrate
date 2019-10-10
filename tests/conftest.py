import pytest

from django.core.management import call_command
from django.db import connection
from django.db.migrations.executor import MigrationExecutor


@pytest.fixture()
def get_migration_executor():
    return lambda: MigrationExecutor(connection, progress_callback=None)


@pytest.fixture()
def django_db_setup(django_db_blocker, get_migration_executor):
    with django_db_blocker.unblock():
        targets = get_migration_executor().loader.graph.leaf_nodes()

        # Remove default 'home' target and add a custom target
        targets = [target for target in targets if target[0] != "home"]
        targets.append(("home", "0002_homepage_body"))

        get_migration_executor().migrate(targets)
        call_command("flush", "--noinput")
        call_command("loaddata", "testapp/testdata.json")
