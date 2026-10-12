from number_theory.gcd import gcd
from number_theory.lcm import lcm
from number_theory.modular_inverse import modular_inverse_euclidean
from number_theory.primality import is_prime_6k


def generate_keys_totient(p: int, q: int, e: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Generate RSA public and private keys from two distinct primes.

    Validate the prime factors and public exponent, then compute
    the RSA modulus, Euler's totient, and private exponent.

    Args:
        p (int): First prime number.
        q (int): Second prime number, distinct from p.
        e (int): Public exponent coprime to Euler's totient.

    Returns:
        tuple[tuple[int, int], tuple[int, int]]: A pair containing
            the public key (N, e) and private key (N, d).

    Raises:
        ValueError: If p or q is not prime, if the primes are
            equal, or if the public exponent is invalid.
    """
    if not is_prime_6k(p) or not is_prime_6k(q):
        raise ValueError("p and q must be prime numbers")

    if p == q:
        raise ValueError("p and q must be distinct prime numbers")

    N = p * q
    phi_n = (p - 1) * (q - 1)

    if not 1 < e < phi_n:
        raise ValueError("e must satisfy 1 < e < phi(N)")

    if gcd(e, phi_n) != 1:
        raise ValueError("e must be coprime to phi(N)")

    d = modular_inverse_euclidean(e, phi_n)

    public_key = (N, e)
    private_key = (N, d)

    return (public_key, private_key)


def generate_keys_carmichael(
    p: int, q: int, e: int
) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Generate RSA public and private keys using Carmichael's function.

    Validate two distinct prime factors and the public exponent.
    Compute the RSA modulus and derive the private exponent
    using the modular inverse of e modulo Carmichael's lambda.

    For distinct prime factors p and q, Carmichael's function
    is computed as lambda(N) = lcm(p - 1, q - 1).

    Args:
        p (int): First prime number.
        q (int): Second prime number, distinct from p.
        e (int): Public exponent coprime to Carmichael's lambda.

    Returns:
        tuple[tuple[int, int], tuple[int, int]]: A tuple containing
            the public key (N, e) and private key (N, d).

    Raises:
        ValueError: If p and q are not distinct primes or
            if the public exponent is invalid.
    """
    if not is_prime_6k(p) or not is_prime_6k(q):
        raise ValueError("p and q must be prime numbers")

    if p == q:
        raise ValueError("p and q must be distinct prime numbers")

    N = p * q
    carmichael_n = lcm(p-1, q-1)

    if not 1 < e < carmichael_n:
        raise ValueError("e must satisfy 1 < e < carmichael(N)")

    if gcd(e, carmichael_n) != 1:
        raise ValueError("e must be coprime to carmichael(N)")

    d = modular_inverse_euclidean(e, carmichael_n)

    public_key = (N, e)
    private_key = (N, d)

    return (public_key, private_key)