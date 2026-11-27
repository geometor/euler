:navigation: header
:order: 1
:type: book
:title: An Easy Solution of Certain Very Difficult Geometric Problems
:nav_title: Easy Solution
:breadcrumb_title: Easy Solution
:layout: book
:book_title: An Easy Solution of Certain Very Difficult Geometric Problems
:book_subtitle: Solutio facilis problematum quorumdam geometricorum difficillimorum (1765)
:author: Leonhard Euler
:year: 1765
:tracks: English: index | Latin: title-la
:excerpt: Euler's 1765 St. Petersburg memoir discovering the Euler line connecting the orthocenter, centroid, and circumcenter of every triangle, deriving the six mutual quadrances among the four classical triangle centers, and solving the inverse reconstruction problem via symmetric polynomials.

.. _solutio_facilis_1765-index:
.. _euler-1765-index:

An Easy Solution of Certain Very Difficult Geometric Problems
=============================================================

.. rubric:: *Solutio facilis problematum quorumdam geometricorum difficillimorum* — :person:`Leonhard Euler <euler>` (1765, Eneström **E325**)

.. container:: title-page

   | **Author:** :person:`Leonhard Euler <euler>`
   | **First Edition (Latin, 1767):** *Novi Commentarii Academiae Scientiarum Imperialis Petropolitanae*, Tom. XI pro Anno MDCCLXV, Petropoli: Typis Academiae Scientiarum, MDCCLXVII, pp. 103–123, Tab. II Fig. 1–9 (*Opera Omnia*, Ser. I, Vol. 26, pp. 139–157).
   | **English Translation:** Original folio-verified translation curated for the GEOMETOR Digital Scriptorium.
   | **Synchronized 4-Track Codex:** *English · Latin · Summary · Notes*, paired with exact symbolic verification in :mod:`geometor.euler`.

.. epigraph::

   „Tum vero omnibus difficultatibus feliciter superatis insignes quaedam affectiones inter illa quatuor puncta se prodent, quarum cognitio in Geometria haud leuis momenti est censenda.“

   “Moreover, once all difficulties have been happily overcome, certain remarkable properties among those four points reveal themselves, the knowledge of which must be judged of no small importance in Geometry.”

   — :person:`Leonhard Euler <euler>`, :cite:`*Solutio facilis* <euler_1765>`, § 3 (p. 104)

----

.. _table-of-contents:

Table of Contents
-----------------

.. container:: toc-outline

   - **§§ 1–9 — The Four Classical Triangle Centers & Orthogonal Coordinates** *(pp. 103–107)*
     (:ref:`English <euler-01-en>` · :ref:`Latin <euler-01-la>` · :ref:`Summary <euler-01-summary>` · :ref:`Notes <euler-01-notes>`)

     Enumeration of the four classical concurrency centers :math:`E = X(4)` (orthocenter), :math:`F = X(2)` (centroid), :math:`G = X(1)` (incenter), and :math:`H = X(3)` (circumcenter), formulation of the inverse determination problem, and derivation of their rational orthogonal coordinates on base :math:`AB = c`.

   - **§§ 10–18 — Symmetric Polynomials, Six Mutual Quadrances & The Euler Line** *(pp. 107–114)*
     (:ref:`English <euler-02-en>` · :ref:`Latin <euler-02-la>` · :ref:`Summary <euler-02-summary>` · :ref:`Notes <euler-02-notes>`)

     Change of variables to the :term:`elementary symmetric polynomials <symmetric-polynomials>` :math:`p = a+b+c`, :math:`q = ab+ac+bc`, :math:`r = abc`, symmetric Heron expansion :math:`16A^2 = -p^4 + 4p^2q - 8pr`, closed-form derivation of all six squared inter-center distances (Formulas I–VI), discovery of the :term:`Euler Line <euler-line>` (:math:`FH = \tfrac{1}{2}EF`, :math:`EH = \tfrac{3}{2}EF`), and the compatibility law :math:`4GH^2 + 2EG^2 = 3EF^2 + 6FG^2`.

   - **§§ 19–24 — The Inverse Reconstruction Problem & Side-Length Cubic** *(pp. 114–118)*
     (:ref:`English <euler-03-en>` · :ref:`Latin <euler-03-la>` · :ref:`Summary <euler-03-summary>` · :ref:`Notes <euler-03-notes>`)

     Reduction of the inverse problem (“given the four centers :math:`E, F, G, H`, construct the triangle”) to auxiliary invariants :math:`P = p^2`, :math:`Q = r/p`, :math:`R = r^2/(4A^2)`, exact cancellation of the quadratic term :math:`Q^2` yielding rational :math:`(P, q, Q)`, Viète's cubic :math:`z^3 - pz^2 + qz - r = 0`, and the integer benchmark :math:`(5, 6, 7) \implies z^3 - 18z^2 + 107z - 210 = 0`.

   - **§§ 25–34 — Collinear Centers, Isosceles Degeneracy & Casus Irreducibilis** *(pp. 118–123)*
     (:ref:`English <euler-04-en>` · :ref:`Latin <euler-04-la>` · :ref:`Summary <euler-04-summary>` · :ref:`Notes <euler-04-notes>`)

     Analysis of the degenerate case in which :math:`G` lies on the Euler line :math:`EH` (forcing an isosceles triangle with rational root :math:`z = c`), the four positional regimes relative to midpoint :math:`I`, symmetric parameterization by :math:`(e, f, k) = (EG, GH, EH)`, reality *diorismos* inequalities, and angle trisection in the :term:`casus irreducibilis <casus-irreducibilis>`.

.. picture:: /_static/constructions/euler_1765_centers.svg
   :alt: Euler's four classical triangle centers X(1), X(2), X(3), X(4) and the Euler line on the (15, 13, 14) triangle

.. collection::
   :sort: order

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Title Pages

   title-la
