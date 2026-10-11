from rsa.message_encoding import encode_message, split_message
from number_theory.modular_exponentiation import modular_pow_fast


def rsa_encrypt(message: str, public_key: tuple[int, int]) -> list[int]:
    """
    Encrypt an uppercase text message using textbook RSA.

    Encode the message as two-digit decimal character codes,
    split it into blocks smaller than the RSA modulus, and
    encrypt each block using fast modular exponentiation.

    Args:
        message (str): Uppercase text containing only letters A-Z.
        public_key (tuple[int, int]): RSA public key (N, e).

    Returns:
        list[int]: Encrypted integer blocks in their original order.

    Raises:
        ValueError: If the message contains unsupported characters,
            the RSA modulus is too small, or the public key
            contains invalid values.
    """
    N, e = public_key

    if N <= 35:
        raise ValueError("RSA modulus must be greater than 35")

    if e <= 0:
        raise ValueError("Public exponent must be positive")

    if not message:
        raise ValueError("Message must not be empty")

    encoded = encode_message(message)
    blocks = split_message(encoded, N)

    encrypted_blocks = []

    for block in blocks:
        encrypted = modular_pow_fast(block, e, N)
        encrypted_blocks.append(encrypted)

    return encrypted_blocks