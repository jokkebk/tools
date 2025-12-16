#!/usr/bin/env python3
import json
import subprocess
from datetime import datetime

def get_github_url():
    """
    Get the GitHub repository URL from git remote configuration.
    """
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True,
        )
        url = result.stdout.strip()
        if url.startswith("git@"):
            # Converts git@github.com:user/repo.git to https://github.com/user/repo
            url = url.replace("git@github.com:", "https://github.com/")
        if url.endswith(".git"):
            url = url[:-4]
        return url
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Could not get git remote URL.")
        return None

def main():
    github_url = get_github_url()
    if not github_url:
        print("Could not determine GitHub URL. Links to commits will not be generated.")

    try:
        with open("tools.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("tools.json not found. Please run gather_tools.py first.")
        return
    except json.JSONDecodeError:
        print("Could not parse tools.json.")
        return

    pages = data.get("pages", {})
    tools = []
    for filename, details in pages.items():
        if "last_commit" in details:
            commit = details["last_commit"]
            tool_name = filename.replace(".html", "")
            tools.append({
                "name": tool_name,
                "filename": filename,
                "commit_hash": commit["hash"],
                "commit_date": commit["date"],
                "commit_message": commit["message"],
            })

    if not tools:
        print("No tools found in tools.json.")
        with open("README.md", "w") as f:
            f.write("# Tools Index\n\nNo tools found.\n")
        return
        
    # Sort tools alphabetically for the index
    sorted_alpha = sorted(tools, key=lambda x: x["name"])

    # Sort tools by date for the detailed list
    for tool in tools:
        tool['commit_date_parsed'] = datetime.fromisoformat(tool['commit_date'])

    sorted_date = sorted(tools, key=lambda x: x['commit_date_parsed'], reverse=True)


    # Generate Markdown
    md_content = "# Tools Index\n\n"

    md_content += "## Alphabetical Index\n\n"
    for tool in sorted_alpha:
        md_content += f"* [{tool['name']}]({tool['filename']})\n"

    md_content += "\n## Tools\n\n"
    for tool in sorted_date:
        md_content += f"### [{tool['name']}]({tool['filename']})\n\n"
        
        md_content += f"> last updated: {tool['commit_date_parsed'].strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        message_lines = tool['commit_message'].strip().split('\n')
        for line in message_lines:
            md_content += f"> {line}\n"
        md_content += ">\n"

        if github_url:
            md_content += f"> [view commit]({github_url}/commit/{tool['commit_hash']})\n"
        
        md_content += "\n"


    with open("README.md", "w") as f:
        f.write(md_content)

    print("README.md generated successfully.")


if __name__ == "__main__":
    main()
