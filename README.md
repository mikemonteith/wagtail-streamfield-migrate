# wagtail-streamfield-migrate

Migrating streamfield data in wagtail can be difficult.
If you change or rename your streamfield blocks, custom migations are required to
iterate through page models and alter streamfield data to prevent data loss.

This wagtail plugin aims to make custom streamfield migrations easy.

## Contributing

### Formatting

`black .`

### Linting

`flake8 .`

### Tests

`pytest`
