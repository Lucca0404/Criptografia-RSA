import pytest

from rsa.key_generation import generate_keys_totient
from rsa.encryption import rsa_encrypt
from rsa.decryption import rsa_decrypt


@pytest.mark.parametrize(
    "message",
    [
        "A",
        "Z",
        "RSA",
        "CASA",
        "HELLO",
        "MATEMATICA",
        "CRIPTOGRAFIA",
        "TEORIADOSNUMEROS",
    ],
)
def test_rsa_decryption(message):
    """
    Test RSA decryption using equivalence partitioning
    and round-trip testing.

    Cover single-character and multi-character messages,
    including messages requiring multiple encrypted blocks.

    Verify that encryption followed by decryption
    recovers the original plaintext.
    """
    public_key, private_key = generate_keys_totient(61, 53, 17)

    ciphertext = rsa_encrypt(message, public_key)
    decrypted = rsa_decrypt(ciphertext, private_key)

    assert decrypted == message


@pytest.mark.parametrize(
    "ciphertext, private_key",
    [
        ([], (3233, 2753)),
        ([100], (35, 3)),
        ([100], (3233, 0)),
        ([100], (3233, -1)),
        ([-1], (3233, 2753)),
        ([3233], (3233, 2753)),
        ([4000], (3233, 2753)),
        (["ABC"], (3233, 2753)),
    ],
)
def test_rsa_decryption_invalid_inputs(ciphertext, private_key):
    """
    Verify that RSA decryption rejects invalid inputs.

    Test empty ciphertexts, malformed encrypted blocks,
    invalid block ranges, and invalid private keys.
    """
    with pytest.raises(ValueError):
        rsa_decrypt(ciphertext, private_key)


@pytest.mark.parametrize(
    "p, q, e, message",
    [
        (61, 53, 17, "RSA"),
        (11, 13, 7, "CASA"),
        (17, 19, 5, "MATEMATICA"),
        (23, 29, 3, "CRIPTOGRAFIA"),
    ],
)
def test_rsa_round_trip_different_keys(p, q, e, message):
    """
    Verify RSA encryption and decryption with different keys.

    Test that valid key pairs recover the original message
    independently of the selected prime factors.
    """
    public_key, private_key = generate_keys_totient(p, q, e)

    ciphertext = rsa_encrypt(message, public_key)

    assert rsa_decrypt(ciphertext, private_key) == message