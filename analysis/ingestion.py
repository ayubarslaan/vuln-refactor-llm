"""Code ingestion and parsing scaffold using AST/Tree-sitter."""

def parse_structure(source_code: str) -> dict:
    """Return structural metadata extracted from source code."""
    return {"length": len(source_code)}
