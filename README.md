# CLI Inventory Management System

A command-line inventory and order management system built in Python with SQLite, developed to practice software feature testing, data validation, and structured reporting.

## Features
- Add items, add/remove stock
- Place and cancel orders (with automatic stock adjustment)
- Low stock report
- Most-ordered items report (SQL aggregation)
- Full input validation with clear error handling

## Tech stack
- Python 3
- SQLite (built-in `sqlite3`)
- pytest (testing)
- python-dotenv (configuration)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. (Optional) Copy `.env.example` to `.env` to configure the database path:
```bash
cp .env.example .env
```

3. Run the program:
```bash
python main.py
```
This automatically creates the database and tables on first run.

## Running tests
```bash
pytest tests/ -v
```
Tests run against a separate `inventory_test.db`, never against a real data — each test starts from a clean, empty database.

## Project structure
```
├── main.py           # entry point — sets up DB, starts the CLI
├── cli.py             # command-line menu and user interaction
├── inventory.py        # core business logic (items, orders, reports)
├── db_setup.py          # database schema and migration
├── db_conection.py       # database connection helper
├── requirements.txt
├── .env.example
└── tests/
    ├── conftest.py        # test database fixture
    └── test_inventory.py   # test suite (31 tests)
```

## Testing approach
See `report.md` for the full findings write-up, including test coverage breakdown and a before/after comparison demonstrating regression detection.