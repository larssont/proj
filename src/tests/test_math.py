from hypothesis import given
from hypothesis import strategies as st

from num.some import add_numbers, sub_numbers


@given(st.floats(), st.floats())
def test_add(a: float, b: float):
    add_numbers(a, b)


@given(st.floats(), st.floats())
def test_sub(a: float, b: float):
    sub_numbers(a, b)
