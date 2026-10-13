import pytest

from number_theory.modular_exponentiation import (
    modular_pow_linear,
    modular_pow_fast,
)


@pytest.mark.parametrize(
    "algorithm",
    [
        modular_pow_linear,
        modular_pow_fast,
    ],
)
@pytest.mark.parametrize(
    "base, exponent, modulus, expected",
    [
        (3, 13, 7, 3),       # General case
        (2, 10, 1000, 24),  # Power greater than modulus
        (5, 0, 13, 1),      # Zero exponent
        (0, 5, 7, 0),       # Zero base
        (1, 100, 17, 1),    # Multiplicative identity
        (7, 1, 10, 7),      # Exponent equal to one
        (10, 3, 5, 0),      # Base divisible by modulus
        (5, 3, 1, 0),       # Modulus equal to one
        (-2, 3, 5, 2),      # Negative base
        (2, 20, 17, 16),    # Larger exponent
    ],
)
def test_modular_exponentiation(
    algorithm, base, exponent, modulus, expected
):
    """
    Test modular exponentiation using equivalence partitioning
    and boundary value analysis.

    The test cases cover the following categories:
        - Positive and negative bases.
        - Zero and positive exponents.
        - Modulus equal to one.
        - Bases divisible by the modulus.
        - Powers greater than the modulus.

    Verify that both implementations return the expected
    modular exponentiation result.
    """
    assert algorithm(base, exponent, modulus) == expected


@pytest.mark.parametrize(
    "algorithm",
    [
        modular_pow_linear,
        modular_pow_fast,
    ],
)
@pytest.mark.parametrize(
    "base, exponent, modulus",
    [
        (2, -1, 7),     # Negative exponent
        (2, 5, 0),      # Zero modulus
        (2, 5, -7),     # Negative modulus
    ],
)
def test_modular_exponentiation_invalid_inputs(
    algorithm, base, exponent, modulus
):
    """
    Test whether modular exponentiation rejects invalid arguments.

    Verify that negative exponents and non-positive moduli
    raise ValueError.
    """
    with pytest.raises(ValueError):
        algorithm(base, exponent, modulus)


@pytest.mark.parametrize(
    "base, exponent, modulus",
    [
        (3, 13, 7),
        (7, 100, 40),
        (11, 256, 97),
        (17, 1000, 101),
        (123, 500, 997),
    ],
)
def test_modular_exponentiation_consistency(
    base, exponent, modulus
):
    """
    Verify consistency between modular exponentiation algorithms.

    Compare both implementations against Python's built-in
    modular exponentiation function.
    """
    expected = pow(base, exponent, modulus)

    assert modular_pow_linear(base, exponent, modulus) == expected
    assert modular_pow_fast(base, exponent, modulus) == expected