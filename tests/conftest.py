import pytest
from django.core.management import call_command
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from wagtail.core.models import Page


@pytest.fixture()
def get_migration_executor():
    return lambda: MigrationExecutor(connection, progress_callback=None)


@pytest.fixture(scope="function")
def transactional_db(transactional_db, django_db_blocker):
    with django_db_blocker.unblock():
        migration_executor = MigrationExecutor(connection, progress_callback=None)
        targets = migration_executor.loader.graph.leaf_nodes()

        # Remove default 'home' target and add a custom target
        targets = [target for target in targets if target[0] != "home"]
        targets.append(("home", "0002_homepage_body"))

        migration_executor.migrate(targets)
        call_command("flush", "--noinput")


@pytest.fixture
def root_page():
    return Page.objects.create(title="Root", slug="root", path="0001", depth=1)


@pytest.fixture()
def fully_migrated(get_migration_executor):
    targets = [("home", "0003_rename_title_to_heading")]
    get_migration_executor().migrate(targets)
