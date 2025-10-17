# Learning-Object-Oriented-Python

![](https://www.codetriage.com/josharsh/learning-object-oriented-python/badges/users.svg)
![Tests](https://github.com/josharsh/OPython-Init/workflows/Run%20Tests/badge.svg)

This repository walks you through the Object Oriented Programming in python. Illustrates real world examples, working codes and going about finding a coding solution.

## 🧪 Testing Framework

This repository includes a comprehensive test suite to ensure code quality and help learners understand Test-Driven Development (TDD).

### Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
python -m unittest discover -s tests -p "test_*.py" -v

# Or use pytest
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=Examples --cov-report=html
```

### CI/CD

All tests run automatically on every push and pull request via GitHub Actions. See `.github/workflows/tests.yml` for details. 

