def modular_pow_linear(
    base: int, exponent: int, modulus: int
) -> int:
    """
    Compute modular exponentiation using repeated multiplication.

    Calculate (base ** exponent) % modulus by multiplying
    the base successively and applying modular reduction.

    The algorithm has O(exponent) time complexity and
    O(1) auxiliary space complexity.

    Args:
        base (int): Integer base of the exponentiation.
        exponent (int): Non-negative integer exponent.
        modulus (int): Positive integer modulus.

    Returns:
        int: The result of modular exponentiation.

    Raises:
        ValueError: If exponent is negative or modulus is not positive.
    """
    if exponent < 0:
        raise ValueError("exponent must be a non-negative integer")

    if modulus <= 0:
        raise ValueError("modulus must be a positive integer")

    result = 1 % modulus
    base %= modulus

    i = 0

    while i < exponent:
        result = (result * base) % modulus
        i += 1

    return result


def modular_pow_fast(
    base: int, exponent: int, modulus: int
) -> int:
    """
    Compute modular exponentiation using exponentiation by squaring.

    Calculate (base ** exponent) % modulus by repeatedly
    squaring the base and halving the exponent.

    The algorithm has O(log exponent) time complexity and
    O(1) auxiliary space complexity.

    Args:
        base (int): Integer base of the exponentiation.
        exponent (int): Non-negative integer exponent.
        modulus (int): Positive integer modulus.

    Returns:
        int: The result of modular exponentiation.

    Raises:
        ValueError: If exponent is negative or modulus is not positive.
    """
    if exponent < 0:
        raise ValueError("exponent must be a non-negative integer")

    if modulus <= 0:
        raise ValueError("modulus must be a positive integer")

    result = 1 % modulus
    base %= modulus 

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus

        base = (base * base) % modulus
        exponent //= 2

    return result