import numpy as np

from simple_functions import my_sin


class TestSin(object):
    ''' Class to test if sin approximation is working as intended'''

    def test_sin(self):
        x = 2*np.pi
        sin_approx = my_sin(x, 100)
        assert np.isclose(sin_approx, np.sin(x), atol=1.0e-12)
