import os.path as op
import numpy as np
import numpy.testing as npt
import mancala

data_path = op.join(mancala.__path__[0], 'data')

def test_dummy():
    a = 1.0
    npt.assert_equal(a,1.0)
