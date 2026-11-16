"""Comprehensive test suite for geometor.euler.

Verifies:
1. 100% exact symbolic zero residuals across Euler (1765) identities.
2. Exact cubic reconstruction on Euler's (5, 6, 7) triangle and canonical (15, 13, 14) triangle.
3. Exact sympy.Rational coordinates for X(1)..X(4) with strict zero-Float enforcement
   across every element in Model.
4. Clean CLI execution and version check.
"""

from __future__ import annotations

import pytest
import sympy as sp
from geometor.model import Model

from geometor.euler import (
    __version__,
    construct_euler_1765_centers,
    prove_euler_1765_identities,
    run,
    solve_euler_reconstruction_cubic,
)


def _assert_zero_floats_in_model(model: object) -> None:
    """Ensure no sympy.Float atoms exist anywhere in constructed Model points or circles."""
    assert isinstance(model, Model)
    for pt in model.points:
        assert not pt.x.atoms(sp.Float), f"Float found in point {model[pt].ID}.x: {pt.x}"
        assert not pt.y.atoms(sp.Float), f"Float found in point {model[pt].ID}.y: {pt.y}"
    for circ in model.circles:
        assert not circ.radius.atoms(sp.Float), f"Float found in circle {model[circ].ID} radius"


def test_version_and_cli() -> None:
    """Verify initial semantic version and clean zero-argument CLI execution."""
    assert __version__ == "0.1.0"
    assert run([]) == 0


def test_cli_help_exits_cleanly() -> None:
    """Verify ``--help`` exits cleanly with code ``0``."""
    with pytest.raises(SystemExit) as exc_info:
        run(["--help"])
    assert exc_info.value.code == 0


def test_symbolic_identities_euler() -> None:
    """All polynomial identities of Euler (1765) cancel to exact 0."""
    report = prove_euler_1765_identities()
    assert report.all_verified
    assert len(report.symbolic_residuals) >= 26
    for name, residual in report.symbolic_residuals.items():
        assert residual == sp.Integer(0), f"Non-zero residual for {name}: {residual}"


def test_euler_cubic_reconstruction_567_and_heronian() -> None:
    """Euler's §§ 21–24 reconstruction recovers z^3 - 18z^2 + 107z - 210 = 0 on (5, 6, 7)."""
    report = prove_euler_1765_identities()
    cub = report.euler_cubic_567
    assert cub.p_sum == sp.Integer(18)
    assert cub.q_pairs == sp.Integer(107)
    assert cub.r_prod == sp.Integer(210)
    assert cub.recovered_roots == (sp.Integer(5), sp.Integer(6), sp.Integer(7))

    # Also reconstruct (15, 13, 14) -> sorted roots (13, 14, 15)
    h = report.heronian_15_13_14
    assert h.area == sp.Integer(84)
    assert h.circumradius == sp.Rational(65, 8)
    assert h.inradius == sp.Integer(4)

    p_h, q_h, r_h, _, roots_h = solve_euler_reconstruction_cubic(
        h.quadrances_euler["EF2"],
        h.quadrances_euler["FG2"],
        h.quadrances_euler["GH2"],
    )
    assert (p_h, q_h, r_h) == (sp.Integer(42), sp.Integer(587), sp.Integer(2730))
    assert roots_h == (sp.Integer(13), sp.Integer(14), sp.Integer(15))

    with pytest.raises(ValueError, match="Incompatible distances"):
        solve_euler_reconstruction_cubic(
            h.quadrances_euler["EF2"],
            h.quadrances_euler["FG2"],
            h.quadrances_euler["GH2"],
            eg_sq=sp.Integer(999),
        )


def test_construct_euler_1765_centers_exact_rational() -> None:
    """Euler's four centers land on exact rational coordinates with zero floats."""
    res = construct_euler_1765_centers()
    _assert_zero_floats_in_model(res.model)

    assert (res.x1_incenter_G.x, res.x1_incenter_G.y) == (sp.Integer(6), sp.Integer(4))
    assert (res.x2_centroid_F.x, res.x2_centroid_F.y) == (sp.Rational(19, 3), sp.Integer(4))
    assert (res.x3_circumcenter_H.x, res.x3_circumcenter_H.y) == (
        sp.Integer(7),
        sp.Rational(33, 8),
    )
    assert (res.x4_orthocenter_E.x, res.x4_orthocenter_E.y) == (
        sp.Integer(5),
        sp.Rational(15, 4),
    )
