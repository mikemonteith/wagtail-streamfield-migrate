# wagtail-streamfield-migrate

Migrating streamfield data in wagtail can be difficult.
If you change or rename your streamfield blocks, custom migations are required to
iterate through page models and alter streamfield data to prevent data loss.

This wagtail plugin aims to make custom streamfield migrations easy.

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
