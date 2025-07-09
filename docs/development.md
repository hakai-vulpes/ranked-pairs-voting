# Development Setup Guide

This guide helps you set up a development environment for the Ranked Pairs Voting package.

## Prerequisites

- Python 3.9 or higher
- Git
- pip (usually comes with Python)

## Quick Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/danielnavarropuche/ranked-pairs-voting.git
   cd ranked-pairs-voting
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the package in development mode**:
   ```bash
   pip install -e .
   ```

4. **Install development dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run all tests and measure performance
python -m pytest tests/ --durations=0

# Run tests with coverage (requires pytest-cov)
pip install pytest-cov  # Install if not already installed
python -m pytest tests/ --cov=rankedpairsvoting --cov-report=html --cov-report=term

# Alternative coverage commands
python -m pytest tests/ --cov=rankedpairsvoting --cov-report=term-missing
python -m pytest tests/ --cov=rankedpairsvoting --cov-report=html

# Run specific test file
python -m pytest tests/test_rankedpairsvoting.py

# Run with verbose output
python -m pytest tests/ -v

# Run tests and generate coverage report in HTML format
python -m pytest tests/ --cov=rankedpairsvoting --cov-report=html
# Then open htmlcov/index.html in your browser
```

### Code Formatting

```bash
# Format code with Black
black rankedpairsvoting/ tests/

# Check formatting (dry run)
black --check rankedpairsvoting/ tests/
```

### Linting

```bash
# Run flake8 linter
flake8 rankedpairsvoting/ tests/

# Tests ran by actions in Github (necessary for pull requests)
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

### Type Checking

```bash
# Run mypy type checker
mypy rankedpairsvoting/

# Check specific file
mypy rankedpairsvoting/main.py
```

### Interactive Testing

Create a test script to experiment with the package:

```python
# test_interactive.py
from rankedpairsvoting import ranked_pairs_voting

# Test with your own data
candidates = ['Alice', 'Bob', 'Charlie']
votes = [
    [1, 2, 3],
    [2, 1, 3], 
    [1, 3, 2],
]

result = ranked_pairs_voting(candidates, votes)
print(f"Winner: {result[0]}")
print(f"Full ranking: {result}")
```

Then run:
```bash
python test_interactive.py
```

## Package Structure

```
ranked-pairs-voting/
├── rankedpairsvoting/               # Main package
│   ├── __init__.py                 # Package initialization
│   ├── main.py                     # Main voting function
│   └── objects.py                  # Graph data structure
├── tests/                          # Test suite
│   ├── __init__.py
│   └── test_rankedpairsvoting.py
├── docs/                            # Documentation
│   ├── api.md                      # API reference
│   ├── development.md              # You are here!
│   ├── examples.md                 # Usage examples
│   └── mathematical-background.md  # Theoretical background and complexity analysis
│
├── README.md                       # Main documentation
├── CONTRIBUTING.md                 # Contribution guidelines
├── CHANGELOG.md                    # Version history
├── LICENSE                         # MIT license
├── pyproject.toml                  # Package configuration
├── gitignore                       # Generated gitignore for Python and VSCode
└── .flake8                         # Flake8 configuration (compatibility with black)
```

## Building the Package

### For Development

```bash
# Install in editable mode
pip install -e .
```

### For Distribution

```bash
# Install build tools
pip install build

# Build the package
python -m build

# This creates:
# dist/rankedpairsvoting-0.0.1.tar.gz
# dist/rankedpairsvoting-0.0.1-py3-none-any.whl
```

### Publishing (Maintainers Only)

```bash
# Install twine
pip install twine

# Upload to PyPI test
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## Debugging Tips

### Common Issues

1. **Import errors**: Make sure you've installed the package with `pip install -e .`
2. **Test failures**: Check that you're in the virtual environment
3. **Type errors**: Ensure you have the latest version of mypy
4. **Coverage not working**: 
   - Ensure `pytest-cov` is installed: `pip install pytest-cov`
   - Make sure you're running from the project root directory
   - Check that the package is installed in editable mode: `pip install -e .`
   - If coverage shows 0%, the source path might be wrong

### Fixing Coverage Issues

If coverage tests aren't working, try these solutions:

```bash
# 1. Reinstall the package in editable mode
pip uninstall rankedpairsvoting
pip install -e .

# 2. Install coverage dependencies
pip install pytest-cov coverage

# 3. Run coverage with explicit source directory
python -m pytest tests/ --cov=./rankedpairsvoting --cov-report=term-missing

# 4. Alternative: Use coverage directly
coverage run -m pytest tests/
coverage report
coverage html

# 5. Check if the package is properly installed
python -c "import rankedpairsvoting; print(rankedpairsvoting.__file__)"

# 6. Make sure you're in the project root directory
pwd  # Should show your project directory
ls   # Should show rankedpairsvoting/ and tests/ directories
```

**Common Coverage Problems and Solutions:**

1. **"No data to report" error**: 
   - Install the package with `pip install -e .`
   - Make sure you're in the project root directory

2. **Coverage shows 0%**:
   - Check the source path: `--cov=rankedpairsvoting` (not `--cov=./rankedpairsvoting`)
   - Ensure the package is in editable mode

3. **ModuleNotFoundError**:
   - Activate your virtual environment
   - Install the package: `pip install -e .`

4. **Tests not found**:
   - Make sure you're in the project root
   - Check that `tests/` directory exists

### Debugging Test Failures

```bash
# Run with pdb debugger
python -m pytest tests/ --pdb

# Run specific test with debugging
python -m pytest tests/test_rankedpairsvoting.py::TestRankedPairsVoting::test_simple_election -s
```

### Profiling Performance

```python
import cProfile
from rankedpairsvoting import ranked_pairs_voting

# Create large test case
candidates = [f"C{i}" for i in range(20)]
votes = [[i % 20 + 1 for i in range(20)] for _ in range(1000)]

# Profile the function
cProfile.run('ranked_pairs_voting(candidates, votes)')
```

## Documentation

### Viewing Documentation Locally

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Build docs (if using Sphinx in the future)
cd docs/
make html
```

### Testing Documentation Examples

Make sure all code examples in the documentation actually work:

```bash
# Extract and test code examples
python -m doctest README.md
```

## IDE Configuration

### VS Code

Create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests/"]
}
```

### PyCharm

1. Set project interpreter to `./venv/bin/python`
2. Enable pytest as the test runner
3. Configure Black as the formatter
4. Enable flake8 for linting

## Getting Help

- Check the [API documentation](docs/api.md)
- Look at [examples](docs/examples.md)
- Review the [mathematical background](docs/mathematical-background.md)
- Open an issue on GitHub
- Contact the maintainers
