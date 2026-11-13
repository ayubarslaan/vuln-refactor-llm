# Vulnerability Refactor LLM

Automated Code Vulnerability and Refactoring Assistant Using Fine-Tuned Large Language Models.

## Architecture

The project is scaffolded as a modular pipeline:

- `data/`: dataset collection, cleaning, CWE annotation, and formatting into `Input -> Analysis -> Fix` pairs.
- `training/`: fine-tuning pipeline entry points for PyTorch + Hugging Face Transformers/Datasets + PEFT (LoRA/QLoRA).
- `analysis/`: code ingestion/parsing (AST/Tree-sitter) and SAST/dependency scanning wrappers.
- `rag/`: vector database and retrieval components for security guidelines and CWE context.
- `engine/`: inference logic to combine vulnerability context + retrieved knowledge + tuned model output.
- `verification/`: sandbox verification workflow for tests, scan re-checks, patch diffs, and retry/repair loops.
- `app/`: FastAPI backend and minimal web frontend for code upload/repository workflows.
- `tests/`: unit/integration test stubs for preprocessing, inference, and patch validation.

## Project Layout

```text
.
├── analysis/
├── app/
│   ├── backend/
│   └── frontend/
├── data/
├── engine/
├── rag/
├── training/
├── verification/
├── tests/
├── requirements.txt
└── README.md
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run Backend (Scaffold)

```bash
uvicorn app.backend.main:app --reload
```

Health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

## Workflow Overview

1. **Data pipeline** (`data/`): collect and normalize vulnerable/fixed examples, annotate CWE, and format training tuples.
2. **Fine-tuning** (`training/`): train LoRA/QLoRA adapters on code security transformations.
3. **Static analysis ingestion** (`analysis/`): parse source structure and gather SAST/dependency findings.
4. **Retrieval augmentation** (`rag/`): fetch relevant secure-coding guidance and CWE references.
5. **Patch generation** (`engine/`): produce explanations and secure refactoring suggestions.
6. **Verification loop** (`verification/`): execute tests/scans in sandbox and retry on failed validation.
7. **Developer interface** (`app/`): upload code or connect repositories, inspect findings, and accept/reject patches.

## Testing (Scaffold)

```bash
python -m unittest discover -s tests
```

These tests validate scaffold contracts and can be expanded as implementation logic is added.
