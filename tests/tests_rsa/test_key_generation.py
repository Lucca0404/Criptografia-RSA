import pytest

from rsa.key_generation import (
    generate_keys_totient,
    generate_keys_carmichael,
)
from rsa.encryption import rsa_encrypt
from rsa.decryption import rsa_decrypt

from number_theory.gcd import gcd
from number_theory.lcm import lcm


# ============================================================
# 1. EULER'S TOTIENT KEY GENERATION
# ============================================================

@pytest.mark.parametrize(
    "p, q, e, expected_public, expected_private",
    [
        (61, 53, 17, (3233, 17), (3233, 2753)),
        (11, 13, 7, (143, 7), (143, 103)),
        (5, 11, 3, (55, 3), (55, 27)),
        (3, 11, 3, (33, 3), (33, 7)),
    ],
)
def test_generate_keys_totient(
    p, q, e, expected_public, expected_private
):
    """
    Test RSA key generation using Euler's totient function.

    Apply equivalence partitioning to distinct prime pairs
    and valid public exponents.

    Verify the expected public and private key pairs.
    """
    public_key, private_key = generate_keys_totient(p, q, e)

    assert public_key == expected_public
    assert private_key == expected_private


# ============================================================
# 2. CARMICHAEL KEY GENERATION
# ============================================================

@pytest.mark.parametrize(
    "p, q, e, expected_public, expected_private",
    [
        (61, 53, 17, (3233, 17), (3233, 413)),
        (11, 13, 7, (143, 7), (143, 43)),
        (5, 11, 3, (55, 3), (55, 7)),
        (3, 11, 3, (33, 3), (33, 7)),
    ],
)
def test_generate_keys_carmichael(
    p, q, e, expected_public, expected_private
):
    """
    Test RSA key generation using Carmichael's lambda function.

    Apply equivalence partitioning to distinct prime pairs
    and valid public exponents.

    Verify the expected public and private key pairs.
    """
    public_key, private_key = generate_keys_carmichael(p, q, e)

    assert public_key == expected_public
    assert private_key == expected_private


# ============================================================
# 3. INVALID INPUTS
# ============================================================

@pytest.mark.parametrize(
    "algorithm",
    [
        generate_keys_totient,
        generate_keys_carmichael,
    ],
)
@pytest.mark.parametrize(
    "p, q, e",
    [
        (4, 53, 17),     # Composite first factor
        (61, 9, 17),     # Composite second factor
        (61, 61, 17),    # Equal primes
        (1, 53, 17),     # One is not prime
        (0, 53, 17),     # Zero prime factor
        (-5, 53, 17),    # Negative prime factor
        (61, 53, 1),     # Public exponent too small
        (61, 53, 10),    # Public exponent not coprime
        (61, 53, 3120),  # Exponent outside valid range
        (61, 53, 3121),  # Exponent outside valid range
    ],
)
def test_key_generation_invalid_inputs(algorithm, p, q, e):
    """
    Test RSA key generation using equivalence partitioning,
    boundary value analysis, and exception testing.

    Verify that invalid prime factors and public exponents
    raise ValueError in both implementations.
    """
    with pytest.raises(ValueError):
        algorithm(p, q, e)


# ============================================================
# 4. MATHEMATICAL PROPERTIES
# ============================================================

@pytest.mark.parametrize(
    "p, q, e",
    [
        (61, 53, 17),
        (11, 13, 7),
        (5, 11, 3),
        (17, 19, 5),
    ],
)
def test_key_generation_properties(p, q, e):
    """
    Verify the mathematical properties of RSA key generation.

    Check the modulus, public exponent, and multiplicative
    inverse relationships for both key generation methods.
    """
    public_phi, private_phi = generate_keys_totient(p, q, e)
    public_lambda, private_lambda = generate_keys_carmichael(p, q, e)

    N = p * q
    phi_n = (p - 1) * (q - 1)
    lambda_n = lcm(p - 1, q - 1)

    assert public_phi == (N, e)
    assert public_lambda == (N, e)

    d_phi = private_phi[1]
    d_lambda = private_lambda[1]

    assert private_phi[0] == N
    assert private_lambda[0] == N

    assert gcd(e, phi_n) == 1
    assert gcd(e, lambda_n) == 1

    assert (e * d_phi) % phi_n == 1
    assert (e * d_lambda) % lambda_n == 1

    assert (e * d_phi) % lambda_n == 1


# ============================================================
# 5. ENCRYPTION AND DECRYPTION INTEGRATION
# ============================================================

@pytest.mark.parametrize(
    "p, q, e, message",
    [
        (61, 53, 17, "RSA"),
        (61, 53, 17, "MATEMATICA"),
        (11, 13, 7, "CASA"),
        (17, 19, 5, "CRIPTOGRAFIA"),
        (23, 29, 3, "TEORIADOSNUMEROS"),
    ],
)
def test_key_generation_encryption_decryption(p, q, e, message):
    """
    Verify RSA encryption and decryption using both key methods.

    Generate public and private keys with Euler's totient
    and Carmichael's lambda function.

    Verify that both private keys recover the original
    message from the same ciphertext.
    """
    public_phi, private_phi = generate_keys_totient(p, q, e)
    public_lambda, private_lambda = generate_keys_carmichael(p, q, e)

    assert public_phi == public_lambda

    ciphertext = rsa_encrypt(message, public_phi)

    assert rsa_decrypt(ciphertext, private_phi) == message
    assert rsa_decrypt(ciphertext, private_lambda) == message


# ============================================================
# 6. CONSISTENCY BETWEEN KEY GENERATION METHODS
# ============================================================

@pytest.mark.parametrize(
    "p, q, e",
    [
        (61, 53, 17),
        (11, 13, 7),
        (5, 11, 3),
        (17, 19, 5),
        (23, 29, 3),
    ],
)
def test_key_generation_consistency(p, q, e):
    """
    Verify consistency between Euler- and Carmichael-based keys.

    Both methods must produce the same public key.
    Their private exponents must be congruent modulo
    Carmichael's lambda function.
    """
    public_phi, private_phi = generate_keys_totient(p, q, e)
    public_lambda, private_lambda = generate_keys_carmichael(p, q, e)

    lambda_n = lcm(p - 1, q - 1)

    assert public_phi == public_lambda

    d_phi = private_phi[1]
    d_lambda = private_lambda[1]

    assert d_phi % lambda_n == d_lambda