from traffic_heatmap.util import circle
from nose.tools import eq_, ok_


def test_point_in_circle_center():
    ok_(circle.point_in_circle(center=(0, 0), radius=1, point=(0, 0)))


def test_point_in_circle_valid():
    ok_(circle.point_in_circle(center=(0, 0), radius=1, point=(0.25, 0.25)))


def test_point_in_circle_invalid():
    ok_(not circle.point_in_circle(center=(0, 0), radius=1, point=(1, 1)))


def test_generate_grid_simple():
    eq_(list(circle.generate_grid(center=(0, 0), density=1, radius=1)),
        [(0, -1), (-1, 0), (0, 0), (1, 0), (0, 1)])
