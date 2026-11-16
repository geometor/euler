"""Exact symbolic constructions, polynomial proofs, and codex concordance for Leonhard Euler (1765).

Provides:

- :mod:`geometor.euler.euler`: Symbolic SymPy polynomial proofs of Leonhard Euler's 1765/1767
  memoir *Solutio facilis problematum quorumdam geometricorum difficillimorum* (E325, §§ 1–34),
  the six mutual center distances, the Euler line, and the exact compass-and-straightedge
  construction of Euler's four classical centers.
- :mod:`geometor.euler.primitives`: Exact Euclidean compass-and-straightedge sub-constructions.
"""

from __future__ import annotations

from .app import main, run
from geometor.euler.euler import (
    EulerCentersResult,
    EulerCubicExample,
    EulerIdentitiesReport,
    HeronianNumericCheck,
    construct_euler_1765_centers,
    prove_euler_1765_identities,
    solve_euler_reconstruction_cubic,
)
from geometor.euler.primitives import (
    construct_altitude_foot,
    construct_altitude_line,
    construct_angle_bisectors,
    construct_midpoint,
    construct_perp_bisector,
)

__version__ = "0.1.0"

__all__ = [
    "EulerCentersResult",
    "EulerCubicExample",
    "EulerIdentitiesReport",
    "HeronianNumericCheck",
    "__version__",
    "construct_altitude_foot",
    "construct_altitude_line",
    "construct_angle_bisectors",
    "construct_euler_1765_centers",
    "construct_midpoint",
    "construct_perp_bisector",
    "main",
    "prove_euler_1765_identities",
    "run",
    "solve_euler_reconstruction_cubic",
]
