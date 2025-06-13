from hypothesis import given
from hypothesis import strategies as st

from test_new.main import add_numbers


@given(st.floats(), st.floats())
def test_add(a: float, b: float):
    add_numbers(a, b)
