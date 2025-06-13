from hypothesis import given
from hypothesis import strategies as st

from proj._math import add_numbers


@given(st.floats(), st.floats())
def test_add(a: float, b: float):
    add_numbers(a, b)
