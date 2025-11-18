#!/bin/bash
# Generate coverage report for SonarQube

cd "$(dirname "$0")"

# Install coverage.py if needed
python3 -m pip install coverage --break-system-packages -q 2>/dev/null || python3 -m pip install coverage -q 2>/dev/null || true

# Run tests with coverage
python3 -m coverage run --source=src -m unittest tests.test_common_bugs

# Generate XML report for SonarQube
python3 -m coverage xml -o coverage.xml

echo "Coverage report generated: sonarqube_test_samples/coverage.xml"
python3 -m coverage report

