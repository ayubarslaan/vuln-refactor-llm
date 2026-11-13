"""Retrieval module scaffold for CWE/security context."""

def retrieve_security_context(query: str, top_k: int = 5) -> list[dict]:
    """Retrieve relevant security guidance for the query."""
    return [{"query": query, "top_k": top_k, "results": []}]
