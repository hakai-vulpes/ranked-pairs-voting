# Contributing to Ranked Pairs Voting

Thank you for your interest in contributing to the Ranked Pairs Voting package! This document provides guidelines for contributing to the project.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git

### Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/hakai-vulpes/ranked-pairs-voting.git
   cd ranked-pairs-voting
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the package in development mode:
   ```bash
   pip install -e .
   ```

5. Install development dependencies:
   ```bash
   pip install pytest black flake8 mypy
   ```

## Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes
- Keep functions focused and concise

### Code Formatting

Use Black for code formatting:
```bash
black rankedpairsvoting/
```

### Linting

Check code quality with flake8:
```bash
flake8 rankedpairsvoting/
```

### Type Checking

Run mypy for type checking:
```bash
mypy rankedpairsvoting/
```

## Testing

### Running Tests

Run the test suite:
```bash
python -m pytest tests/
```

### Writing Tests

- Write tests for all new functionality
- Ensure edge cases are covered
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern

Example test structure:
```python
def test_ranked_pairs_basic_election():
    # Arrange
    candidates = ['Alice', 'Bob', 'Charlie']
    votes = [[1, 2, 3], [2, 1, 3], [1, 3, 2]]
    
    # Act
    result = ranked_pairs_voting(candidates, votes)
    
    # Assert
    assert result[0] == 'Alice'  # Alice should win
    assert len(result) == 3
```

## Pull Request Process

1. Create a feature branch from main:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

3. Run tests and ensure they pass:
   ```bash
   python -m pytest tests/
   ```

4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request on GitHub

### Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Ensure all tests pass
- Update documentation if necessary
- Keep changes focused and atomic

## Reporting Issues

When reporting issues, please include:

- Python version
- Package version
- Minimal code example that reproduces the issue
- Expected vs. actual behavior
- Full error traceback if applicable

## Feature Requests

We welcome feature requests! Please:

- Check if the feature already exists
- Provide a clear use case
- Explain the expected behavior
- Consider the impact on existing functionality

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment for all contributors

## Questions?

If you have questions about contributing, feel free to:

- Open an issue for discussion
- Contact the maintainers
- Check existing documentation

Thank you for contributing to Ranked Pairs Voting!
