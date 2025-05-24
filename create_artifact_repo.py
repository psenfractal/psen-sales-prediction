import subprocess
import json

REPO_NAME = "psen-sales-prediction"
LOCATION = "us-central1"

def repository_exists(name, location):
    try:
        result = subprocess.run(
            ["gcloud", "artifacts", "repositories", "list", f"--location={location}", "--format=json"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        repos = json.loads(result.stdout)
        return any(repo["name"].endswith(f"/{name}") for repo in repos)
    except subprocess.CalledProcessError as e:
        print("Failed to list repositories:", e.stderr)
        return False

def create_repository(name, location):
    print(f"Creating repository: {name}")
    try:
        subprocess.run([
            "gcloud", "artifacts", "repositories", "create", name,
            "--repository-format=docker",
            f"--location={location}",
            '--description=Docker repo for Cloud Run images'
        ], check=True)
        print("Repository created successfully.")
    except subprocess.CalledProcessError as e:
        print("Error creating repository:", e.stderr)

if __name__ == "__main__":
    if repository_exists(REPO_NAME, LOCATION):
        print(f"Repository '{REPO_NAME}' already exists.")
    else:
        create_repository(REPO_NAME, LOCATION)
