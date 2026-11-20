<a href="https://geometor.github.io/euler/"><img src="docsrc/_static/logo.png" alt="GEOMETOR • euler Medallion" align="right" width="150"></a>

# GEOMETOR • euler

**Visit the Online Archive:** https://geometor.github.io/euler/

<p align="center">
  <a href="https://geometor.github.io/euler/"><img src="docsrc/_static/constructions/euler_1765_centers.svg" alt="GEOMETOR • euler featured geometric construction"></a>
</p>

**Leonhard Euler • Solutio facilis problematum geometricorum (E325) • semantic digital archive**

## Mission

`geometor/euler` is part of the interconnected [GEOMETOR](https://geometor.com) semantic digital archive. It liberates Leonhard Euler's landmark 1765 memoir *Solutio facilis problematum quorumdam geometricorum difficillimorum* (Eneström E325) from isolated print bounds into addressable semantic units, calibrated theme-adaptive vector diagrams, primary-source folio provenance, and exact symbolic proofs establishing the Euler line across the GEOMETOR corpus.

## Books in This Archive

- [An Easy Solution of Certain Very Difficult Geometric Problems](https://geometor.github.io/euler/solutio_facilis_1765/) — Euler's celebrated 1765 St. Petersburg memoir (*Solutio facilis problematum quorumdam geometricorum difficillimorum*) discovering the collinearity of the orthocenter $H$, centroid $G$, and circumcenter $O$, and the distance invariant $HG = 2GO$.

## Repository Contents

- `docsrc/` — Book Codex tracks, apparatus registries, and Sphinx docs compiled by [PHOTON publish](https://github.com/photon-platform/publish).
- `resources/` — Primary folio scans, structure maps, persons/citations registries, and review manifests.
- `src/geometor/euler/` — Symbolic geometry models, algebraic verification scripts, and apparatus compilation helpers.

## Local Build & Verification

```bash
publish build
uv run --no-sync pytest
```
## Part of the GEOMETOR Knowledge Archive

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
