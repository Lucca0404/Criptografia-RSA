from number_theory.gcd import gcd
from number_theory.extended_gcd import extended_gcd_iterative
from number_theory.totient import euler_totient_sqrtn
from number_theory.modular_exponentiation import modular_pow_fast


def modular_inverse_euclidean(n: int, m: int) -> int:
    """
    Compute the modular multiplicative inverse using
    the Extended Euclidean Algorithm.

    Find the Bézout coefficient associated with n and
    reduce it modulo m to obtain the canonical inverse.

    Args:
        n (int): Positive integer whose inverse is to be computed.
        m (int): Modulus greater than one.

    Returns:
        int: The multiplicative inverse of n modulo m.

    Raises:
        ValueError: If either input is outside the valid domain
            or if n and m are not coprime.
    """
    if n <= 0 or m <= 1:
        raise ValueError("n must be positive and m greater than one")

    d, x, y = extended_gcd_iterative(n, m)

    if d != 1:
        raise ValueError("Modular inverse does not exist")

    return x % m


def modular_inverse_euler(n: int, m: int) -> int:
    """
    Compute the modular multiplicative inverse using Euler's theorem.

    Apply Euler's totient function and fast modular
    exponentiation to calculate the inverse.

    Args:
        n (int): Positive integer whose inverse is to be computed.
        m (int): Modulus greater than one.

    Returns:
        int: The multiplicative inverse of n modulo m.

    Raises:
        ValueError: If either input is outside the valid domain
            or if n and m are not coprime.
    """
    if n <= 0 or m <= 1:
        raise ValueError("n must be positive and m greater than one")

    if gcd(n, m) != 1:
        raise ValueError("Modular inverse does not exist")

    phi_m = euler_totient_sqrtn(m)

    return modular_pow_fast(n, phi_m - 1, m)