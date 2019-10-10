import pytest
from home.models import HomePage, HomePageAfterMigration


@pytest.mark.django_db(transaction=True)
def test_block_type_change(settings, get_migration_executor):
    get_migration_executor().migrate([("home", "0003_rename_title_to_heading")])
    homepage = HomePageAfterMigration.objects.first()
    heading_block = homepage.body[0]
    assert heading_block.block_type == "heading"
    assert heading_block.value == "Heading 1"


@pytest.mark.django_db(transaction=True)
def test_reverse_block_type_change(settings, get_migration_executor):
    # migrate up
    get_migration_executor().migrate([("home", "0003_rename_title_to_heading")])
    # migrate down
    get_migration_executor().migrate([("home", "0002_homepage_body")])

    homepage = HomePage.objects.first()
    heading_block = homepage.body[0]
    assert heading_block.block_type == "title"
    assert heading_block.value == "Heading 1"
