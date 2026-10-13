import pytest

from number_theory.modular_inverse import (
    modular_inverse_euclidean,
    modular_inverse_euler,
)


@pytest.mark.parametrize(
    "algorithm",
    [
        modular_inverse_euclidean,
        modular_inverse_euler,
    ],
)
@pytest.mark.parametrize(
    "n, m, expected",
    [
        (3, 11, 4),     # Prime modulus
        (7, 40, 23),    # Composite modulus
        (5, 12, 5),     # Self-inverse element
        (10, 17, 12),   # Prime modulus
        (1, 13, 1),     # Multiplicative identity
        (17, 43, 38),   # Coprime integers
        (3, 2, 1),      # Smallest valid modulus
    ],
)
def test_modular_inverse(algorithm, n, m, expected):
    """
    Test modular inverse algorithms using equivalence partitioning
    and boundary value analysis.

    The test cases cover the following categories:
        - Prime and composite moduli.
        - Coprime integers.
        - Self-inverse elements.
        - The multiplicative identity.
        - The smallest valid modulus.

    Verify that both implementations return the expected
    modular multiplicative inverse.
    """
    assert algorithm(n, m) == expected


@pytest.mark.parametrize(
    "algorithm",
    [
        modular_inverse_euclidean,
        modular_inverse_euler,
    ],
)
@pytest.mark.parametrize(
    "n, m",
    [
        (6, 9),       # Non-coprime integers
        (10, 20),     # Non-coprime integers
        (0, 7),       # Zero input
        (-3, 11),     # Negative input
        (3, 1),       # Invalid modulus
        (3, 0),       # Zero modulus
        (3, -7),      # Negative modulus
    ],
)
def test_modular_inverse_invalid_inputs(algorithm, n, m):
    """
    Verify that modular inverse algorithms reject invalid inputs.

    Test non-coprime integers and inputs outside the
    supported domain using exception testing.
    """
    with pytest.raises(ValueError):
        algorithm(n, m)


@pytest.mark.parametrize(
    "n, m",
    [
        (3, 11),
        (7, 40),
        (11, 26),
        (13, 37),
        (17, 100),
        (23, 101),
    ],
)
def test_modular_inverse_properties(n, m):
    """
    Verify the multiplicative inverse property and consistency.

    Check that both algorithms return the same inverse and
    satisfy the modular multiplicative identity.
    """
    inverse_euclidean = modular_inverse_euclidean(n, m)
    inverse_euler = modular_inverse_euler(n, m)

    assert inverse_euclidean == inverse_euler
    assert (n * inverse_euclidean) % m == 1
    assert (n * inverse_euler) % m == 1