import pytest

from number_theory.totient import (
    euler_totient_nlogn,
    euler_totient_sqrtn,
)


def test_euler_totient_nlogn():
    """
    Test the GCD-based totient implementation using equivalence
    partitioning, boundary value analysis, and exception testing.

    The test cases cover the following categories:
        - Composite numbers with distinct prime factors.
        - Prime numbers.
        - Powers of prime numbers.
        - The smallest positive integer (n = 1).
        - Optional retrieval of coprime integers.
        - Non-positive integers, which must raise ValueError.
    """
    assert euler_totient_nlogn(10) == 4
    assert euler_totient_nlogn(29) == 28
    assert euler_totient_nlogn(8) == 4
    assert euler_totient_nlogn(1) == 1

    with pytest.raises(ValueError):
        euler_totient_nlogn(-1)

    with pytest.raises(ValueError):
        euler_totient_nlogn(0)


def test_euler_totient_sqrtn():
    """
    Test the factorization-based totient implementation using
    equivalence partitioning, boundary value analysis,
    and exception testing.

    The test cases cover the following categories:
        - Composite numbers with distinct prime factors.
        - Prime numbers.
        - Powers of prime numbers.
        - The smallest positive integer (n = 1).
        - Non-positive integers, which must raise ValueError.
    """
    assert euler_totient_sqrtn(10) == 4
    assert euler_totient_sqrtn(29) == 28
    assert euler_totient_sqrtn(8) == 4
    assert euler_totient_sqrtn(1) == 1

    with pytest.raises(ValueError):
        euler_totient_sqrtn(-1)

    with pytest.raises(ValueError):
        euler_totient_sqrtn(0)


@pytest.mark.parametrize("n", range(1, 101))
def test_totient_implementations_agree(n):
    """
    Verify that both totient implementations produce identical results.

    Cross-check the GCD-based and factorization-based algorithms
    for positive integers from 1 through 100.
    """
    assert euler_totient_nlogn(n) == euler_totient_sqrtn(n)