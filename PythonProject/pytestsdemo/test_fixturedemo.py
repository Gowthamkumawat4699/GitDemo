import pytest


def test_fixturedemo1(setup):
    print('I am going print in the middle')


#output
# command - py.test test_fixturedemo.py -v -s
# test_fixturedemo.py::test_fixturedemo1 I am going to print at first
# I am going print in the middle
# PASSEDI am going to print at last

