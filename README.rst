GEOMETOR • euler
================

**Visit the Online Archive:** https://geometor.github.io/euler/

.. image:: docsrc/_static/constructions/euler_1765_centers.svg
   :alt: GEOMETOR • euler featured geometric construction
   :target: https://geometor.github.io/euler/
   :align: center

**Leonhard Euler • Solutio facilis problematum geometricorum (E325) • semantic digital archive**

Mission
-------

``geometor/euler`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It liberates Leonhard Euler's landmark 1765 memoir *Solutio facilis problematum quorumdam geometricorum difficillimorum* (Eneström E325) from isolated print bounds into addressable semantic units, calibrated theme-adaptive vector diagrams, primary-source folio provenance, and exact symbolic proofs establishing the Euler line across the GEOMETOR corpus.

Books in This Archive
---------------------

- `An Easy Solution of Certain Very Difficult Geometric Problems <https://geometor.github.io/euler/solutio_facilis_1765/>`_ — Euler's celebrated 1765 St. Petersburg memoir (*Solutio facilis problematum quorumdam geometricorum difficillimorum*) discovering the collinearity of the orthocenter :math:`H`, centroid :math:`G`, and circumcenter :math:`O`, and the distance invariant :math:`HG = 2GO`.

Python Package & Modules
------------------------

The ``geometor-euler`` Python package (``import geometor.euler``) provides the executable symbolic geometry, construction, and compilation modules powering this archive:

- ``euler.py`` — Symbolic proofs and Euclidean construction for Euler's 1765 memoir (E325) and Feuerbach (1822).
- ``primitives.py`` — Euclidean compass-and-straightedge sub-constructions for triangle geometry.
- ``app.py`` — Command-line interface for ``geometor.euler``.

See the `API Reference <https://geometor.github.io/euler/modules/>`_ for full module documentation.

Repository Contents
-------------------

- ``docsrc/`` — Book Codex tracks, apparatus registries, and Sphinx docs compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Primary folio scans, structure maps, persons/citations registries, and review manifests.
- ``src/geometor/euler/`` — Symbolic geometry models, algebraic verification scripts, and apparatus compilation helpers.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
