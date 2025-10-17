# Test Suite for OPython-Init

This directory contains comprehensive unit tests for all example code in the repository.

## Running Tests

### Run all tests with unittest:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Run all tests with pytest:
```bash
pytest tests/ -v
```

### Run a specific test file:
```bash
python -m unittest tests/test_stack.py -v
```

### Run with coverage:
```bash
pytest tests/ -v --cov=Examples --cov-report=html
```

## Test Files

- `test_basic_class.py` - Tests for basic Person class
- `test_stack.py` - Tests for Stack data structure
- `test_linkedlist.py` - Tests for LinkedList implementation
- `test_calculator.py` - Tests for Calculator class
- `test_circular_queue.py` - Tests for CircularQueue
- `test_graph.py` - Tests for Graph algorithms (BFS, DFS)
- `test_inheritance.py` - Tests for inheritance concepts
- `test_comprehensive_example.py` - Tests for BankAccount example

## CI/CD

Tests run automatically on every push and pull request via GitHub Actions.
See `.github/workflows/tests.yml` for configuration.

## Contributing

When adding new example code, please also add corresponding unit tests following the existing pattern.
