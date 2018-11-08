"""
=================================
Exercise 7: Zonotope transformers
=================================

**Problem 1.** Design a sound and precise ReLU transformer for zonotopes.

**Problem 2.** Prove the soundness of the transformer.

**Problem 3.** Implement in Python the following zonotope transformers:

1. Dot product with a constant vector:

  - Input: constants (c\ :sub:`1`, ..., c\ :sub:`n`), zonotopes (z\ :sub:`1`, ..., z\ :sub:`n`)
  - Output: the zonotope c\ :sub:`1` z\ :sub:`1` + ... + c\ :sub:`n` z\ :sub:`n`

2. Your ReLU transformer from Problem 1.

You can use the provided template below.

**Problem 4.** Run the neural network from Exercise 6 with your zonotopes.
"""

from collections import defaultdict


class ZonotopeContext:
    """Zonotope context.

    A zonotope context creates and transforms zonotopes.  Each zonotope is
    represented as a dictionary.  The items of the dictionary are pairs::

        (i, a)

    where ``i`` is the index of a noise symbol and ``a`` is the respective
    coefficient for that noise symbol.  The free coefficient is represented
    as the noise symbol with index 0, that is the pair ``(0, a)``.

    Parameters
    ----------
    n : int
        Number of noise symbols in pre-existing zonotopes.
    """

    def __init__(self, n=0):
        self.n = n

    def make(self, m, d):
        """Create a zonotope.

        The zonotope is specified with two parameters.

        Parameters
        ----------
        m : float
            Midpoint.
        d : float
            Maximum distance from midpoint.

        Returns
        -------
        zonotope

        Examples
        --------
        >>> ctx = ZonotopeContext()
        >>> sorted(ctx.make(1.0, 0.25).items())
        [(0, 1.0), (1, 0.25)]
        """
        assert d >= 0.0
        z = defaultdict(float, {0: float(m)})
        if d > 0:
            self.n += 1
            z[self.n] = float(d)
        return z

    def extrema(self, z):
        """Compute zonotope extrema.

        Parameters
        ----------
        z : zonotope

        Returns
        -------
        float tuple
            The minimum and the maximum.

        Examples
        --------
        >>> ctx = ZonotopeContext(3)
        >>> ctx.extrema({0: 14.0, 1: 0.25, 2: 0.5, 3: 0.75})
        (12.5, 15.5)
        """
        min = 0
        max = 0
        for k, v in z.items():
            if k != 0:
                min -= abs(v)
                max += abs(v)
                
        return (z[0] + min, z[0] + max)
        

    def dot(self, C, Z):
        """Compute dot product.

        Parameters
        ----------
        C : float list
        Z : zonotope list

        Returns
        -------
        zonotope

        Examples
        --------
        >>> ctx = ZonotopeContext()
        >>> C = [1.0,
        ...      2.0,
        ...      3.0]
        >>> Z = [ctx.make(1.0, 0.25),
        ...      ctx.make(2.0, 0.25),
        ...      ctx.make(3.0, 0.25)]
        >>> sorted(ctx.dot(C, Z).items())
        [(0, 14.0), (1, 0.25), (2, 0.5), (3, 0.75)]
        """
        zonotop = defaultdict(float)
        assert len(C) == len(Z)
        for c, z in zip(C, Z):
            for k, v in z.items():
                zonotop[k] += v*c
                
        return zonotop

    def relu(self, z):
        """Compute ReLU.

        Parameters
        ----------
        z : zonotope

        Returns
        -------
        zonotope

        Examples
        --------
        >>> ctx = ZonotopeContext(3)
        >>> sorted(ctx.relu({0: 14.0, 1: 0.25, 2: 0.5, 3: 0.75}).items())
        [(0, 14.0), (1, 0.25), (2, 0.5), (3, 0.75)]
        >>> sorted(ctx.relu({0: -14.0, 1: 0.25, 2: 0.5, 3: 0.75}).items())
        [(0, 0.0)]
        >>> sorted(ctx.relu({0: 0.000, 1: 0.25, 2: 0.5, 3: 0.75}).items())
        [(0, 0.375), (1, 0.125), (2, 0.25), (3, 0.375), (4, 0.375)]
        """
        assert isinstance(z, dict)
        l, u = self.extrema(z)
        
        if u <= 0:
            return self.make(0, 0)
        
        elif l > 0:
            return z
        
        else:
            m = (u)/(u-l)
            b = -0.5 * m * l
            return self.dot([m, b], [z, self.make(1.0, 1.0)])
