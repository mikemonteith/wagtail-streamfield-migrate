import pytest
from home.models import HomePageAfterMigration


@pytest.mark.django_db(transaction=True)
def test_block_type_change(settings, migrate):
    migrate.migrate([("home", "0003_rename_title_to_heading")])
    homepage = HomePageAfterMigration.objects.first()
    heading_block = homepage.body[0]
    assert heading_block.block_type == "heading"
    assert heading_block.value == "Heading 1"
