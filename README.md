# wagtail-streamfield-migrate

Migrating streamfield data in wagtail can be difficult.
If you change or rename your streamfield blocks, custom migations are required to
iterate through page models and alter streamfield data to prevent data loss.

This wagtail plugin aims to make custom streamfield migrations easy.

## Usage

If you have changed a streamfield definition, django will create a migration file for you via the [makemigrations](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-makemigrations) management command.
Wagtail will not migrate the streamfield data for you, you must add your own data migration manually.

Add a `StreamfieldMigrate` operation before the `AlterField` operation on your streamfield.

```py
from django.db import migrations

from wagtailstreamfieldmigrate import StreamfieldMigration

def forwards(stream_data):
    # Write custom logic here to alter the raw stream_data
    return stream_data

def backwards(stream_data):
    # Write custom logic here to alter the raw stream_data
    return stream_data

class Migration(migrations.Migrate):

    dependencies = [
        ...
    ]

    operations = [
        StreamfieldMigrate('home', 'homepage', 'body', forwards, backwards), # Add this line
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=...
        )
    ]

```

## Contributing

### Getting started

1. Clone the repo `git clone https://github.com/mikemonteith/wagtail-streamfield-migrate.git`
2. Install dependencies `pip install -e .[testing]`

### Formatting

`black .`

### Linting

`flake8 .`

### Tests

`pytest`
