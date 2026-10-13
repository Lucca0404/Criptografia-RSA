import pytest

from rsa.encryption import rsa_encrypt
from rsa.message_encoding import encode_message, split_message
from number_theory.modular_exponentiation import modular_pow_fast


@pytest.mark.parametrize(
    "message, public_key",
    [
        ("A", (3233, 17)),
        ("RSA", (3233, 17)),
        ("CASA", (3233, 17)),
        ("MATEMATICA", (3233, 17)),
        ("HELLO", (3233, 17)),
        ("Z", (55, 3)),
    ],
)
def test_rsa_encryption(message, public_key):
    """
    Test textbook RSA encryption using equivalence partitioning.

    Cover single-character and multi-character messages,
    different public keys, and multiple plaintext blocks.

    Verify that each encrypted block matches modular
    exponentiation of the corresponding plaintext block.
    """
    N, e = public_key

    encoded = encode_message(message)
    plaintext_blocks = split_message(encoded, N)

    encrypted_blocks = rsa_encrypt(message, public_key)

    assert len(encrypted_blocks) == len(plaintext_blocks)

    for plaintext, ciphertext in zip(
        plaintext_blocks, encrypted_blocks
    ):
        assert ciphertext == modular_pow_fast(plaintext, e, N)
        assert 0 <= ciphertext < N


@pytest.mark.parametrize(
    "message, public_key",
    [
        ("hello", (3233, 17)),
        ("HELLO WORLD", (3233, 17)),
        ("RSA!", (3233, 17)),
        ("", (3233, 17)),
        ("RSA", (35, 17)),
        ("RSA", (3233, 0)),
        ("RSA", (3233, -1)),
    ],
)
def test_rsa_encryption_invalid_inputs(message, public_key):
    """
    Verify that textbook RSA encryption rejects invalid inputs.

    Test unsupported characters, empty messages,
    insufficient modulus size, and invalid public exponents.
    """
    with pytest.raises(ValueError):
        rsa_encrypt(message, public_key)