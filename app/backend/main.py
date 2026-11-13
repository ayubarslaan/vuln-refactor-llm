"""FastAPI backend scaffold for vulnerability assistant workflows."""

from fastapi import FastAPI, UploadFile

app = FastAPI(title="Vulnerability and Refactoring Assistant")


@app.get("/health")
def health() -> dict:
    """Basic health endpoint."""
    return {"status": "ok"}


@app.post("/upload")
async def upload_code(file: UploadFile) -> dict:
    """Accept uploaded source archives or files for analysis."""
    return {"filename": file.filename, "accepted": True}
