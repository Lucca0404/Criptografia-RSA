from number_theory.primality import is_prime_6k
from number_theory.modular_exponentiation import modular_pow_fast


def legendre_symbol(a: int, p: int) -> int:
    """
    Compute the Legendre symbol (a/p) using Euler's criterion.

    The Legendre symbol determines whether an integer a is a
    quadratic residue modulo an odd prime p.

    Euler's criterion states that:
        a^((p-1)/2) ≡ (a/p) (mod p).

    Args:
        a (int): Integer whose quadratic residuosity is tested.
        p (int): Odd prime number used as the modulus.

    Returns:
        int: The Legendre symbol (a/p):
            0 if p divides a.
            1 if a is a quadratic residue modulo p.
           -1 if a is a quadratic non-residue modulo p.

    Raises:
        ValueError: If p is not an odd prime number.

    Time Complexity:
        O(log p) modular multiplications when using binary
        modular exponentiation.
    """
    if p <= 2 or not is_prime_6k(p):
        raise ValueError("p must be a odd prime integer")

    result = modular_pow_fast(a,(p-1)//2, p)

    if result == p - 1:
        result = -1

    return result
