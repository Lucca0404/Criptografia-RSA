import pytest

from rsa.message_encoding import (
    encode_message,
    split_message,
    join_blocks,
    decode_message,
)


@pytest.mark.parametrize(
    "message, expected",
    [
        ("A", "10"),
        ("Z", "35"),
        ("RSA", "272810"),
        ("CASA", "12102810"),
        ("HELLO", "1714212124"),
    ],
)
def test_encode_message(message, expected):
    """
    Test message encoding using equivalence partitioning.

    Verify individual letters, boundary characters,
    and multi-character messages.
    """
    assert encode_message(message) == expected


@pytest.mark.parametrize(
    "encoded, modulus, expected",
    [
        ("12102810", 3233, [1210, 2810]),
        ("1011", 100, [10, 11]),
        ("1011", 2000, [1011]),
        ("35", 36, [35]),
    ],
)
def test_split_message(encoded, modulus, expected):
    """
    Verify that encoded messages are divided into valid RSA blocks.

    Test different modulus sizes while preserving
    two-digit character boundaries.
    """
    assert split_message(encoded, modulus) == expected


@pytest.mark.parametrize(
    "message, modulus",
    [
        ("RSA", 3233),
        ("CASA", 100),
        ("HELLO", 10000),
        ("MATHEMATICS", 100000),
        ("Z", 36),
    ],
)
def test_message_round_trip(message, modulus):
    """
    Verify that encoding, splitting, joining, and decoding
    preserve the original message.
    """
    encoded = encode_message(message)
    blocks = split_message(encoded, modulus)

    assert all(0 <= block < modulus for block in blocks)
    assert decode_message(join_blocks(blocks)) == message


@pytest.mark.parametrize(
    "message",
    ["hello", "HELLO WORLD", "123", "AÇÃO", "RSA!"],
)
def test_invalid_messages(message):
    """
    Verify that unsupported characters raise ValueError.
    """
    with pytest.raises(ValueError):
        encode_message(message)


@pytest.mark.parametrize(
    "encoded, modulus",
    [
        ("1011", 35),
        ("1011", 0),
        ("101", 3233),
        ("1099", 3233),
    ],
)
def test_invalid_blocks(encoded, modulus):
    """
    Verify that invalid moduli and encoded messages
    raise ValueError.
    """
    with pytest.raises(ValueError):
        split_message(encoded, modulus)