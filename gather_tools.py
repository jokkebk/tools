#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path


def get_last_commit(file_path):
    """
    Get the last commit details for a specific file.
    Returns a dictionary with hash, message, and date, or None.
    """
    try:
        # Get the last commit with its hash, date, and message
        result = subprocess.run(
            ["git", "log", "-n", "1", "--format=%H|%aI|%B", "--", file_path],
            capture_output=True,
            text=True,
            check=True,
        )

        raw_commit = result.stdout.strip()
        if not raw_commit:
            return None

        parts = raw_commit.split("|", 2)
        if len(parts) != 3:
            return None

        commit_hash, commit_date, commit_message = parts
        return {"hash": commit_hash, "date": commit_date, "message": commit_message.strip()}

    except subprocess.CalledProcessError as e:
        print(f"Error getting commit history for {file_path}: {e}")
        return None


def main():
    # Get current directory
    current_dir = Path.cwd()

    # Find all HTML files
    html_files = list(current_dir.glob("*.html"))

    # Dictionary to store results
    results = {"pages": {}}

    # Process each HTML file
    for html_file in html_files:
        file_name = html_file.name
        print(f"Processing {file_name}...")

        # Get last commit details for this file
        last_commit = get_last_commit(html_file)

        if last_commit:
            results["pages"][file_name] = {"last_commit": last_commit}

    # Save results to JSON file
    with open("tools.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"Processed {len(html_files)} files")
    print(f"Found details for {len(results['pages'])} files")
    print("Results saved to tools.json")


if __name__ == "__main__":
    main()
