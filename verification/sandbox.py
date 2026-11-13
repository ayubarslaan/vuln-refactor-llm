"""Docker sandbox verification scaffold."""

def verify_patch(project_path: str) -> dict:
    """Run tests, re-run scans, and return validation metadata."""
    return {"project_path": project_path, "verified": False, "retries": 0}
