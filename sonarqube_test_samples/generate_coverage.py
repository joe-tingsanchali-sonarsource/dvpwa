#!/usr/bin/env python3
"""
Generate coverage report for SonarQube analysis.
This script runs tests with coverage and generates coverage.xml for SonarQube.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and print the result."""
    print(f"\n{description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0 and "coverage" not in cmd:
        print(f"Warning: {description} had issues")
        if result.stderr:
            print(result.stderr)
    return result.returncode == 0

def main():
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("=" * 60)
    print("Generating Coverage Report for SonarQube")
    print("=" * 60)
    
    # Install coverage if needed (suppress errors if already installed)
    run_command(
        "python3 -m pip install coverage --break-system-packages -q 2>/dev/null || "
        "python3 -m pip install coverage -q 2>/dev/null || true",
        "Ensuring coverage.py is installed"
    )
    
    # Run tests with coverage
    print("\nRunning tests with coverage...")
    result = subprocess.run(
        ["python3", "-m", "coverage", "run", "--source=src", "-m", "unittest", "tests.test_common_bugs"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print("Tests failed:")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)
    else:
        print("✓ Tests passed")
    
    # Generate XML report for SonarQube
    run_command(
        "python3 -m coverage xml -o coverage.xml",
        "Generating XML coverage report"
    )
    
    # Display coverage summary
    print("\nCoverage Summary:")
    print("-" * 60)
    subprocess.run(["python3", "-m", "coverage", "report"])
    
    print("\n" + "=" * 60)
    print("✓ Coverage report generated: sonarqube_test_samples/coverage.xml")
    print("=" * 60)
    print("\nYou can now run SonarQube analysis with:")
    print("  sonar-scanner")
    print()

if __name__ == "__main__":
    main()

