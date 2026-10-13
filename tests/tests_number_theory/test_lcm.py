import pytest

from number_theory.lcm import lcm


@pytest.mark.parametrize(
    "n, m, expected",
    [
        (4, 6, 12),      # Non-coprime integers
        (7, 11, 77),     # Coprime prime numbers
        (8, 15, 120),    # Coprime composite numbers
        (5, 5, 5),       # Equal integers
        (3, 12, 12),     # First integer divides the second
        (20, 5, 20),     # Second integer divides the first
        (1, 9, 9),       # Multiplicative identity
        (1, 1, 1),       # Smallest valid inputs
        (12, 18, 36),    # Non-coprime composite numbers
        (13, 17, 221),   # Distinct prime numbers
    ],
)
def test_lcm(n, m, expected):
    """
    Test the LCM function using equivalence partitioning
    and boundary value analysis.

    The test cases cover the following categories:
        - Coprime and non-coprime integers.
        - Prime and composite numbers.
        - Equal integers.
        - Integers where one divides the other.
        - The multiplicative identity (n = 1 or m = 1).
        - The smallest valid inputs.

    Verify that the function returns the expected LCM.
    """
    assert lcm(n, m) == expected


@pytest.mark.parametrize(
    "n, m",
    [
        (0, 5),       # First integer is zero
        (5, 0),       # Second integer is zero
        (0, 0),       # Both integers are zero
        (-5, 10),     # First integer is negative
        (5, -10),     # Second integer is negative
        (-5, -10),    # Both integers are negative
    ],
)
def test_lcm_invalid_inputs(n, m):
    """
    Test whether the LCM function rejects non-positive integers.

    Use equivalence partitioning and exception testing to
    verify that zero and negative inputs raise ValueError.
    """
    with pytest.raises(ValueError):
        lcm(n, m)