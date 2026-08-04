# File purpose: Thin setuptools shim so legacy `setup.py` callers still work.
# Primary components: setuptools.setup() deferred entirely to pyproject.toml.
# I/O: Invoked by older tooling; modern builds should use `python -m build`.

from setuptools import setup

setup()
