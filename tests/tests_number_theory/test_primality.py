import pytest

from number_theory.primality import (
    is_prime_traditional,
    is_prime_odd,
    is_prime_6k,
)


@pytest.mark.parametrize(
    "algorithm",
    [
        is_prime_traditional,
        is_prime_odd,
        is_prime_6k,
    ],
)
@pytest.mark.parametrize(
    "n, expected",
    [
        (-7, False),     # Negative integer
        (0, False),      # Zero
        (1, False),      # Multiplicative identity
        (2, True),       # Smallest prime
        (3, True),       # Odd prime
        (4, False),      # Even composite
        (9, False),      # Odd perfect square
        (25, False),     # Square of a prime
        (49, False),     # Square of a prime
        (97, True),      # Prime number
        (121, False),    # Square of 11
        (9973, True),    # Larger prime
    ],
)
def test_primality(algorithm, n, expected):
    """
    Test primality algorithms using equivalence partitioning
    and boundary value analysis.

    The test cases cover the following categories:
        - Negative integers, zero, and one.
        - Prime and composite integers.
        - Even and odd integers.
        - Perfect squares of prime numbers.
        - Small and relatively large prime numbers.

    Verify that all implementations correctly classify
    integers according to their primality.
    """
    assert algorithm(n) == expected