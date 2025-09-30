"""Test configuration for pytest.

Ensure the project's `src` directory is on sys.path during test collection so
CI runners (or any environment that doesn't set PYTHONPATH) can import the
package modules as `calculator.*`.
"""

import os
import sys

# Compute absolute path to the src directory and insert it at the front of sys.path
ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
if os.path.isdir(SRC) and SRC not in sys.path:
    sys.path.insert(0, SRC)
