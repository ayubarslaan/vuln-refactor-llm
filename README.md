# Automated Code Vulnerability Detection and Refactoring Assistant

An AI-assisted software security project focused on detecting code vulnerabilities, explaining findings, and helping developers produce safer refactors. The planned system combines a fine-tuned Code LLM, code parsing, security knowledge retrieval, static analysis, and isolated verification.

> **Project status — 13 November 2026:** The FastAPI backend has been started locally and the root route has been accessed. The code-ingestion pipeline is **not yet working end to end**; implementation and debugging are ongoing. UI integration is also in progress. This repository should therefore be treated as an active work in progress, not a completed or production-ready tool.

## Current Progress

| Component | Current status |
| --- | --- |
| FastAPI backend | Starts successfully in the local development environment. |
| Root route | A local `GET /` request has been made. This does not validate the ingestion workflow. |
| Code-ingestion pipeline | **In progress — end-to-end flow is not yet verified.** |
| UI/UX integration | In progress; complete frontend-to-backend integration is not yet confirmed. |
| Vulnerability detection and secure refactoring | Planned system capability; end-to-end functionality has not yet been demonstrated. |
| Fine-tuned Code LLM, RAG, and automated patch verification | Part of the target architecture; implementation and evaluation status should be updated as each component is integrated and tested. |

## Project Goal

Build a workflow that can:

1. Accept a source-code project or repository.
2. Ingest and prepare code for analysis.
3. Identify potentially vulnerable code and explain the relevant security issue.
4. Retrieve relevant secure-coding guidance and vulnerability knowledge.
5. Propose a safer code change.
6. Verify proposed changes using appropriate static checks and tests before presenting them for developer review.

These are target capabilities; they should only be marked complete after their implementation and tests are demonstrated.

## Target Architecture

- **Ingestion layer:** Accept source files/repositories, validate inputs, and prepare code for downstream processing.
- **Code understanding:** Use language-aware parsing (for example, AST or Tree-sitter) to preserve code structure and identify relevant units.
- **Security analysis:** Combine static application security testing (SAST) with model-assisted analysis.
- **Knowledge retrieval:** Use retrieval-augmented generation (RAG) over vulnerability references, CWE guidance, secure-coding patterns, and relevant examples.
- **LLM layer:** Integrate and evaluate a QLoRA fine-tuned Code LLM for vulnerability explanation and patch generation.
- **Verification layer:** Run syntax checks, static analysis, and relevant tests in an isolated execution environment.
- **User interface:** Present ingestion progress, findings, explanations, suggested changes, and verification results.

## Immediate Development Priorities

1. Complete and test the code-ingestion path from input submission through file discovery, parsing/preprocessing, and a structured response.
2. Add clear error handling and useful logs for unsupported files, invalid repositories, and ingestion failures.
3. Connect the working ingestion API to the UI and verify the full frontend-to-backend request flow.
4. Add repeatable tests using a small sample repository and representative source files.
5. Only then connect vulnerability analysis, RAG, model inference, and patch verification incrementally.

## End-to-End Ingestion Acceptance Criteria

The ingestion pipeline should not be considered complete until a test can:

- Submit a supported source-code project through the intended interface or API.
- Validate the input and enumerate supported source files.
- Extract and parse code without silently dropping failures.
- Return a structured result containing processing status and useful file-level information.
- Display that result in the UI.
- Handle invalid input and partial failures with actionable error messages.

## Development Status and Contributions

This project is under active development. Features described in the target architecture are goals, not claims of completed functionality. Update the progress table when a component has been implemented and verified with reproducible tests.

