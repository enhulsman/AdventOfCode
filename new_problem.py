#!/usr/bin/env python3
"""
Script to create a new Advent of Code problem directory structure.

Usage:
    python new_problem.py <year> <day> [problem_name]

Examples:
    python new_problem.py 2024 3                    # Automatically fetch problem name
    python new_problem.py 2024 3 TobogganTrajectory # Manually specify problem name
"""

import os
import re
import ssl
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def load_template():
    """
    Load the solution template from the template file.

    Returns:
        The template content as a string, or None if the template file is not found.
    """
    # Get the script's directory (repository root)
    repo_root = Path(__file__).parent
    template_file = repo_root / ".template" / "solution.py"

    try:
        return template_file.read_text()
    except FileNotFoundError:
        print(f"❌ Error: Template file not found at {template_file}")
        print("Please ensure .template/solution.py exists in the repository root.")
        return None

def fetch_problem_name(year, day):
    """
    Fetch the problem name from the Advent of Code website.

    Args:
        year: The year (e.g., 2024)
        day: The day number (e.g., 1-25)

    Returns:
        The problem name with spaces removed (e.g., "RedNosedReports")
        or None if the fetch fails
    """
    url = f"https://adventofcode.com/{year}/day/{day}"

    try:
        print(f"🌐 Fetching problem name from {url}...")

        # Create a request with a user agent to avoid being blocked
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        # Create SSL context that doesn't verify certificates
        # This handles environments where Python doesn't have access to system certs
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        response = urlopen(req, timeout=10, context=context)
        html = response.read().decode('utf-8')

        # Parse the title from the HTML
        # The format is typically: <h2>--- Day X: Problem Name ---</h2>
        match = re.search(r'<h2>---\s*Day\s*\d+:\s*(.+?)\s*---</h2>', html)

        if match:
            problem_title = match.group(1).strip()
            # Remove spaces and special characters to create the directory name
            problem_name = ''.join(problem_title.split())
            # Remove any remaining special characters except alphanumeric
            problem_name = re.sub(r'[^a-zA-Z0-9]', '', problem_name)

            print(f"✅ Found problem: {problem_title}")
            return problem_name
        else:
            print("⚠️  Could not parse problem name from the page")
            return None

    except HTTPError as e:
        if e.code == 404:
            print(f"❌ Problem not found. Day {day} may not be released yet for {year}.")
        else:
            print(f"❌ HTTP Error {e.code}: {e.reason}")
        return None
    except URLError as e:
        print(f"❌ Network error: {e.reason}")
        return None
    except Exception as e:
        print(f"❌ Error fetching problem name: {e}")
        return None

def create_problem_directory(year, day, problem_name, template_content):
    """
    Create a new Advent of Code problem directory with solution and input files.

    Args:
        year: The year (e.g., 2024)
        day: The day number (e.g., 1-25)
        problem_name: The name of the problem (e.g., TobogganTrajectory)
        template_content: The content of the solution template
    """
    # Get the script's directory (repository root)
    repo_root = Path(__file__).parent

    # Create directory path: {year}/{day}-{problem_name}/
    problem_dir = repo_root / str(year) / f"{day}-{problem_name}"

    # Check if directory already exists
    if problem_dir.exists():
        print(f"❌ Error: Directory already exists: {problem_dir}")
        return False

    # Create the directory
    problem_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ Created directory: {problem_dir}")

    # Create solution.py from template
    solution_file = problem_dir / "solution.py"
    solution_file.write_text(template_content)
    print(f"✅ Created solution file: {solution_file}")

    # Create empty input.txt
    input_file = problem_dir / "input.txt"
    input_file.write_text("")
    print(f"✅ Created input file: {input_file}")

    print(f"\n🎄 Ready to solve! Open {problem_dir} and start coding!")
    return True

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python new_problem.py <year> <day> [problem_name]")
        print("\nExamples:")
        print("    python new_problem.py 2024 3                    # Automatically fetch problem name")
        print("    python new_problem.py 2024 3 TobogganTrajectory # Manually specify problem name")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]
    problem_name = sys.argv[3] if len(sys.argv) == 4 else None

    # Validate inputs
    try:
        year_int = int(year)
        day_int = int(day)
        if not (2015 <= year_int <= 2030):
            print("❌ Error: Year should be between 2015 and 2030")
            sys.exit(1)
        if not (1 <= day_int <= 25):
            print("❌ Error: Day should be between 1 and 25")
            sys.exit(1)
    except ValueError:
        print("❌ Error: Year and day must be numbers")
        sys.exit(1)

    # Load the template
    template_content = load_template()
    if not template_content:
        sys.exit(1)

    # Fetch problem name if not provided
    if not problem_name:
        problem_name = fetch_problem_name(year, day)
        if not problem_name:
            print("\n❌ Failed to fetch problem name automatically.")
            print("Please provide the problem name manually:")
            print(f"    python new_problem.py {year} {day} <problem_name>")
            sys.exit(1)

    if not problem_name:
        print("❌ Error: Problem name cannot be empty")
        sys.exit(1)

    # Create the problem directory
    success = create_problem_directory(year, day, problem_name, template_content)

    if success:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
