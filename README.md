# Sudoku Trainer

This is a **fun** *project*!!

## Documentation

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)

## Set-up

1. Install dependencies with:

```bash
poetry install
```

2. Start the app with:

```bash
poetry run invoke start
```

## Command line commands

### Running the app

Run the app with:

```bash
poetry run invoke start
```

### Testing

Run tests with:

```bash
poetry run invoke test
```

### Coverage report

Test coverage report can be generated with:

```bash
poetry run invoke coverage-report
```

Report generates to _htmlcov_ directory.

### Pylint

The checks defined by the file .pylintrc can be performed with the command:

```bash
poetry run invoke lint
```
