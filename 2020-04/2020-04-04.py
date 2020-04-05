import pytest


# content of test_sample.py


def func(x):
    return x + 1


def func1(y):
    return y - 2


def test_answer01():
    assert func(3) == 4


def test_answer02():
    assert func1(8) != 3
