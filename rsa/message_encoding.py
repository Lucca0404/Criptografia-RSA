def encode_message(message: str) -> str:
    """
    Encode uppercase letters as two-digit decimal codes.

    Map letters A-Z to integers 10-35 and concatenate their
    decimal representations.

    Args:
        message (str): Text containing only uppercase letters A-Z.

    Returns:
        str: Concatenated two-digit decimal codes.

    Raises:
        ValueError: If the message contains unsupported characters.
    """
    if not all("A" <= char <= "Z" for char in message):
        raise ValueError("Message must contain only uppercase letters A-Z")

    return "".join(str(ord(char) - ord("A") + 10) for char in message)


def split_message(encoded: str, modulus: int) -> list[int]:
    """
    Split an encoded message into integer blocks smaller than modulus.

    Preserve two-digit character boundaries and maximize the
    number of characters stored in each block.

    Args:
        encoded (str): Concatenated two-digit character codes.
        modulus (int): RSA modulus, which must be greater than 35.

    Returns:
        list[int]: Integer blocks that can be encrypted individually.

    Raises:
        ValueError: If the modulus or encoded message is invalid.
    """
    if modulus <= 35:
        raise ValueError("Modulus must be greater than 35")

    if len(encoded) % 2 != 0:
        raise ValueError("Encoded message must have an even length")

    # Validate character codes before splitting.
    decode_message(encoded)

    blocks = []
    current = ""

    for i in range(0, len(encoded), 2):
        code = encoded[i:i + 2]
        candidate = current + code

        if int(candidate) >= modulus:
            blocks.append(int(current))
            current = code
        else:
            current = candidate

    if current:
        blocks.append(int(current))

    return blocks


def join_blocks(blocks: list[int]) -> str:
    """
    Reconstruct a decimal message from its decrypted integer blocks.

    Args:
        blocks (list[int]): Decrypted blocks containing valid
            two-digit character codes.

    Returns:
        str: Concatenated decimal representation of the message.

    Raises:
        ValueError: If a block contains invalid character codes.
    """
    encoded = ""

    for block in blocks:
        if block < 0:
            raise ValueError("Blocks must be non-negative integers")

        part = str(block)

        if len(part) % 2 != 0:
            raise ValueError("Each block must have an even number of digits")

        decode_message(part)
        encoded += part

    return encoded


def decode_message(encoded: str) -> str:
    """
    Decode a sequence of two-digit decimal codes into uppercase text.

    Convert each code from 10-35 back to its corresponding
    uppercase letter.

    Args:
        encoded (str): Decimal string representing encoded letters.

    Returns:
        str: Decoded uppercase message.

    Raises:
        ValueError: If the input contains invalid codes.
    """
    if len(encoded) % 2 != 0 or not encoded.isdecimal():
        raise ValueError("Encoded message must contain pairs of decimal digits")

    message = ""

    for i in range(0, len(encoded), 2):
        code = int(encoded[i:i + 2])

        if not 10 <= code <= 35:
            raise ValueError("Invalid character code")

        message += chr(ord("A") + code - 10)

    return message