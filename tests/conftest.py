import pytest

from django.core.management import call_command
from django.db import connection
from django.db.migrations.executor import MigrationExecutor


@pytest.fixture()
def django_db_setup(django_db_blocker):
    with django_db_blocker.unblock():
        migration_executor = MigrationExecutor(connection, progress_callback=None)
        targets = migration_executor.loader.graph.leaf_nodes()

        # Remove default 'home' target and add a custom target
        targets = [target for target in targets if target[0] != "home"]
        targets.append(("home", "0002_homepage_body"))

        migration_executor.migrate(targets)
        call_command("flush", "--noinput")
        call_command("loaddata", "testapp/testdata.json")


@pytest.fixture()
def migrate():
    migration_executor = MigrationExecutor(connection, progress_callback=None)
    return migration_executor
