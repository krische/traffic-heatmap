from traffic_heatmap.util import number
from nose.tools import eq_, ok_


def test_is_number_valid_int_string():
    ok_(number.is_number('1'))


def test_is_number_valid_float_string():
    ok_(number.is_number('1.1'))


def test_is_number_invalid_string():
    ok_(number.is_number('hello') is False)


def test_is_number_valid_int():
    ok_(number.is_number(1))


def test_is_number_valid_float():
    ok_(number.is_number(1.1))


def test_is_number_valid_unicode():
    ok_(number.is_number('٥'))


def test_is_number_invalid_unicode():
    ok_(number.is_number('©') is False)


def test_drange_less_than_one():
    eq_(list(number.drange(0, 2, 0.5)), [0, 0.5, 1, 1.5, 2])


def test_drange_greater_than_one():
    eq_(list(number.drange(0, 6, 2)), [0, 2, 4, 6])
