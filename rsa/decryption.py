from number_theory.modular_exponentiation import modular_pow_fast
from rsa.message_encoding import join_blocks, decode_message


def rsa_decrypt(
    ciphertext: list[int],
    private_key: tuple[int, int]
) -> str:
    """
    Decrypt an integer-block ciphertext using textbook RSA.

    Apply fast modular exponentiation to each encrypted block,
    reconstruct the decimal character codes, and decode
    the original uppercase text message.

    Args:
        ciphertext (list[int]): Encrypted integer blocks
            in their original order.
        private_key (tuple[int, int]): RSA private key (N, d).

    Returns:
        str: Decrypted uppercase message containing letters A-Z.

    Raises:
        ValueError: If the ciphertext is empty, contains invalid
            blocks, or if the private key contains invalid values.
    """
    N, d = private_key

    if N <= 35:
        raise ValueError("RSA modulus must be greater than 35")

    if d <= 0:
        raise ValueError("Private exponent must be positive")

    if not ciphertext:
        raise ValueError("Ciphertext must not be empty")

    decrypted_blocks = []

    for block in ciphertext:
        if not isinstance(block, int) or not 0 <= block < N:
            raise ValueError("Encrypted blocks must be integers in [0, N)")

        decrypted = modular_pow_fast(block, d, N)
        decrypted_blocks.append(decrypted)

    encoded = join_blocks(decrypted_blocks)

    return decode_message(encoded)