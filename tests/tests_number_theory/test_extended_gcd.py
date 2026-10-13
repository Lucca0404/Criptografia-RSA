import pytest
from number_theory.gcd import gcd
from number_theory.extended_gcd import extended_gcd_iterative, extended_gcd_recursive


@pytest.mark.parametrize(
    "a, b",
    [
        (35, 12),    # Coprime integers
        (48, 18),    # Non-coprime integers
        (17, 13),    # Distinct prime numbers
        (10, 5),     # One integer divides the other
        (7, 7),      # Equal integers
        (100, 25),   # Exact division
        (0, 7),      # First integer is zero
        (7, 0),      # Second integer is zero
        (0, 0),      # Both integers are zero
    ],
)
def test_extended_gcd_iterative(a, b):
    """
    Test the Extended Euclidean Algorithm using equivalence
    partitioning, boundary value analysis, and property testing.

    The test cases cover the following categories:
        - Coprime and non-coprime integers.
        - Distinct prime numbers.
        - Divisible and equal integers.
        - One or both integers equal to zero.

    Verify that the computed GCD matches the Euclidean algorithm
    and that the returned coefficients satisfy Bézout's identity.
    """
    d, x, y = extended_gcd_iterative(a, b)

    assert d == gcd(a, b)
    assert a * x + b * y == d

def test_extended_gcd_iterative_multiple_inputs():
    """
    Verify Bézout's identity and GCD correctness
    for multiple pairs of positive integers.
    """
    for n in range(1, 101):
        for m in range(1, 101):
            d, x, y = extended_gcd_iterative(n, m)

            assert d == gcd(n, m)
            assert n * x + m * y == d