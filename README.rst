=====
euler
=====

the Swiss mathematician whose 1765 memoir discovered the Euler line connecting the orthocenter, centroid, and circumcenter of every triangle

Edition Overview
----------------

- **Treatise**: *Solutio facilis problematum quorumdam geometricorum difficillimorum*
- **Author**: Leonhard Euler
- **Primary Edition Track**: ``docsrc/solutio_facilis_1765/`` (``:layout: book``)
- **Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
Installation & Verification
---------------------------

Managed with ``uv`` on Python 3.13:

.. code-block:: bash

   uv run --no-sync pytest
   ruff check src tests demos
   publish build

Usage
-----

.. code-block:: bash

   euler --help

Links
-----

- **Documentation**: https://geometor.github.io/euler
- **Repository**: https://github.com/geometor/euler
- **Issues**: https://github.com/geometor/euler/issues

License
-------

Licensed under the MIT License. See ``LICENSE`` for details.
