"""Shared artifact-path resolution for the checks layer.

Every checks-layer artifact reader (``chart_review``, ``claims``, ``dq``,
``figures``) resolves a spec-relative path against the same ordered roots: the
phase directory first (when one is given), then the current working directory.
Keeping that order in one place means a change to root resolution is made once.
"""

from __future__ import annotations

from pathlib import Path


def resolve_roots(phase_dir: str | None) -> list[Path]:
    """Return the search roots for artifact lookup: ``phase_dir`` then cwd."""
    roots: list[Path] = []
    if phase_dir:
        roots.append(Path(phase_dir))
    roots.append(Path.cwd())
    return roots


def find_file(relative: str, roots: list[Path]) -> Path | None:
    """Resolve ``relative`` against ``roots``; ``None`` when nothing exists.

    An absolute path that exists wins outright; otherwise each root is tried in
    order, and finally the path as given (relative to the process cwd).
    """
    candidate = Path(relative)
    if candidate.is_absolute() and candidate.exists():
        return candidate
    for root in roots:
        path = root / relative
        if path.exists():
            return path
    if candidate.exists():
        return candidate
    return None
