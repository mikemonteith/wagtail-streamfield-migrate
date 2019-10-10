import json

import pytest
from wagtail.core.blocks.stream_block import StreamValue
from wagtail.core.models import Page

from home.models import HomePage, HomePageAfterMigration


@pytest.mark.django_db(transaction=True)
def test_block_type_change(root_page, get_migration_executor):
    stream_data = [{"type": "title", "value": "Heading 1"}, {"type": "paragraph", "value": "abcdef"}]
    stream_block = HomePage.body.field.stream_block
    body = StreamValue(stream_block, [], is_lazy=True, raw_text=json.dumps(stream_data))
    root_page.add_child(instance=HomePage(title="test", body=body))

    get_migration_executor().migrate([("home", "0003_rename_title_to_heading")])

    homepage = HomePageAfterMigration.objects.get(title="test")
    heading_block = homepage.body[0]
    assert heading_block.block_type == "heading"
    assert heading_block.value == "Heading 1"


@pytest.mark.django_db(transaction=True)
def test_reverse_block_type_change(root_page, fully_migrated, get_migration_executor):
    stream_data = [{"type": "heading", "value": "Heading 1"}, {"type": "paragraph", "value": "abcdef"}]
    stream_block = HomePageAfterMigration.body.field.stream_block
    body = StreamValue(stream_block, [], is_lazy=True, raw_text=json.dumps(stream_data))
    root_page.add_child(instance=HomePageAfterMigration(title="test", body=body))

    get_migration_executor().migrate([("home", "0002_homepage_body")])

    homepage = HomePage.objects.get(title="test")
    heading_block = homepage.body[0]
    assert heading_block.block_type == "title"
    assert heading_block.value == "Heading 1"
