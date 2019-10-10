import json

from django.db import migrations
from wagtail.core.blocks.stream_block import StreamValue


class StreamfieldMigration(migrations.RunPython):
    def __init__(self, app_label, model_name, field_name, streamfield_forwards=None, streamfield_backwards=None):
        self.app_label = app_label
        self.model_name = model_name
        self.field_name = field_name
        self.streamfield_forwards = streamfield_forwards
        self.streamfield_backwards = streamfield_backwards

        return super().__init__(self.forwards, self.backwards)

    def forwards(self, apps, schema_editor):
        if self.streamfield_forwards is None:
            return
        PageModel = apps.get_model(self.app_label, self.model_name)
        pages = PageModel.objects.all()
        for page in pages:
            stream_data = list(page.body.stream_data)
            stream_data = self.streamfield_forwards(stream_data)
            stream_block = page.body.stream_block
            page.body = StreamValue(stream_block, [], is_lazy=True, raw_text=json.dumps(stream_data))
            page.save()

    def backwards(self, apps, schema_editor):
        if self.streamfield_backwards is None:
            return
        PageModel = apps.get_model(self.app_label, self.model_name)
        pages = PageModel.objects.all()
        for page in pages:
            stream_data = list(page.body.stream_data)
            stream_data = self.streamfield_backwards(stream_data)
            stream_block = page.body.stream_block
            page.body = StreamValue(stream_block, [], is_lazy=True, raw_text=json.dumps(stream_data))
            page.save()
