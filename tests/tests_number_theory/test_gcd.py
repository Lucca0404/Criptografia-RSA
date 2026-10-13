from number_theory.gcd import gcd
import pytest

def test_gcd():
    """
    Test the GCD function using equivalence partitioning,
    boundary value analysis, and exception testing.

    The test cases cover the following categories:
        - Coprime and non-coprime integers.
        - Prime number inputs.
        - One or both integers equal to zero.
        - Negative integers, which must raise ValueError.
    """

    assert gcd(10,5) == 5
    assert gcd(20,3) == 1
    assert gcd(30,0) == 30
    assert gcd(0,0) == 0
    assert gcd(157,29) == 1
    with pytest.raises(ValueError):
        gcd(10,-5)
    with pytest.raises(ValueError):
        gcd(-5,10)