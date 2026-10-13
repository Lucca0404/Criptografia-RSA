import pytest

from number_theory.carmichael import carmichael
from number_theory.totient import euler_totient_sqrtn
from number_theory.lcm import lcm


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),       # Multiplicative identity
        (2, 1),       # Smallest prime
        (3, 2),       # Odd prime
        (5, 4),       # Odd prime
        (7, 6),       # Odd prime
        (4, 2),       # Square of two
        (8, 2),       # Power of two
        (16, 4),      # Higher power of two
        (32, 8),      # Higher power of two
        (9, 6),       # Odd prime power
        (25, 20),     # Odd prime power
        (15, 4),      # Product of distinct primes
        (21, 6),      # Product of distinct primes
        (40, 4),      # Composite number
        (60, 4),      # Multiple prime factors
        (360, 12),    # Multiple prime powers
        (3233, 780),  # RSA modulus
    ],
)
def test_carmichael(n, expected):
    """
    Test Carmichael's lambda function using equivalence
    partitioning and boundary value analysis.

    The test cases cover the following categories:
        - The smallest positive integer.
        - Prime numbers.
        - Powers of two.
        - Odd prime powers.
        - Products of distinct primes.
        - Composite integers with multiple prime factors.
    """
    assert carmichael(n) == expected


@pytest.mark.parametrize("n", range(1, 101))
def test_carmichael_divides_totient(n):
    """
    Verify the divisibility property of Carmichael's function.

    Check that lambda(n) divides phi(n) for positive integers.
    """
    assert euler_totient_sqrtn(n) % carmichael(n) == 0


@pytest.mark.parametrize(
    "p, q",
    [
        (3, 5),
        (5, 7),
        (7, 11),
        (11, 13),
        (53, 61),
    ],
)
def test_carmichael_semiprimes(p, q):
    """
    Verify Carmichael's function for products of distinct primes.

    Check that lambda(p*q) equals lcm(p-1, q-1).
    """
    assert carmichael(p * q) == lcm(p - 1, q - 1)


@pytest.mark.parametrize("n", [0, -1, -2, -10])
def test_carmichael_invalid_inputs(n):
    """
    Verify that Carmichael's function rejects non-positive integers.

    Use boundary value analysis and exception testing.
    """
    with pytest.raises(ValueError):
        carmichael(n)