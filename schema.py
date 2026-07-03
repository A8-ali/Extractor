SCHEMA =

"""
Shared schema definitions for the project.

This module is the single source of truth for the AI output structure.
"""

SCHEMA = {
    "name": str,
    "email": str,
    "age" : int,
    "phone": list[str],
    "linkedin": str,
    "github": str,
    "skills": list[str],
    "education": list[str],
    "experience": list[str],
}

DEFAULT_VALUES = {
    "name": None,
    "email": None,
    "age" : None,
    "phone": [],
    "linkedin": None,
    "github": None,
    "skills": [],
    "education": [],
    "experience": [],
}
