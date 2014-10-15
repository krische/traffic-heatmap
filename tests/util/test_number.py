from traffic_heatmap.util import number
from nose.tools import eq_


def test_drange_less_than_one():
    eq_(list(number.drange(0, 2, 0.5)), [0, 0.5, 1, 1.5, 2])


def test_drange_greater_than_one():
    eq_(list(number.drange(0, 6, 2)), [0, 2, 4, 6])
