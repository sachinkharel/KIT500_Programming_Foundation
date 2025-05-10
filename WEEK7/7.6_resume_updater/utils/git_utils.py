from github import Github
import os
import json
from dotenv import load_dotenv



def push_json_to_github(repo_name, local_json_file, file_path_in_repo, commit_message):
    """
    Push a local JSON file to a GitHub repository.
    Creates the file if it doesn't exist, or updates it if it does.

    Parameters:
    - repo_name (str): Format 'username/repo' (e.g., 'sachinkharel/my-repo')
    - local_json_file (str): Local file path to the JSON file (e.g., 'data.json')
    - file_path_in_repo (str): Path where file should go in the GitHub repo (e.g., 'data/data.json')
    - commit_message (str): Commit message to describe the change
    """
    # Load environment variables from .env
    load_dotenv()
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    # print(f"GitHub Token: {GITHUB_TOKEN}")
    # Authenticate with GitHub using the token from the .env file
    github = Github(GITHUB_TOKEN)
    repo = github.get_repo(repo_name)

    # Load the local JSON file into a Python dictionary
    with open(local_json_file, "r") as f:
        json_data = json.load(f)

    try:
        # Try to get the file from the repo (check if it exists)
        contents = repo.get_contents(file_path_in_repo)

        # If multiple files are returned, find the specific file
        if isinstance(contents, list):
            content_file = next((file for file in contents if file.path == file_path_in_repo), None)
            if not content_file:
                raise FileNotFoundError(f"File {file_path_in_repo} not found in the repository.")
        else:
            content_file = contents

        # If the file exists, update it using its SHA
        repo.update_file(
            path=content_file.path,
            message=commit_message,
            content=json.dumps(json_data, indent=2),  # Format the JSON nicely
            sha=content_file.sha
        )
        print(f"Updated file: {file_path_in_repo}")
    except Exception as e:
        # If the file doesn't exist (404 error), create a new file
        if "404" in str(e):
            repo.create_file(
                path=file_path_in_repo,
                message=commit_message,
                content=json.dumps(json_data, indent=2)
            )
            print(f"Created new file: {file_path_in_repo}")
        else:
            # If some other error occurred, raise it
            print(f"Error: {e}")
