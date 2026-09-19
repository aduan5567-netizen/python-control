import numpy as np
from matplotlib.transforms import Affine2D, Bbox

from control.grid import ModifiedExtremeFinderCycle


def test_modified_extreme_finder_cycle():
    finder = ModifiedExtremeFinderCycle(
        20, 20, lon_cycle=360, lat_cycle=None,
        lon_minmax=(90, 270), lat_minmax=(0, np.inf))

    limits = finder(lambda x, y: (x, y), 90, 0, 270, 1)
    np.testing.assert_allclose(limits, (90, 270, 0, 1.05))

    transformed_bbox = finder._find_transformed_bbox(
        Affine2D(), Bbox.from_extents(90, 0, 270, 1))
    np.testing.assert_allclose(
        transformed_bbox.extents, (90, 0, 270, 1.05))
