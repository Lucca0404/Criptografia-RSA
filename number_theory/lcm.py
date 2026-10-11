from number_theory.gcd import gcd


def lcm(n: int, m: int) -> int:
    """
    Compute the least common multiple (LCM) of two positive integers.

    Use the relationship between the GCD and LCM to calculate
    the smallest positive integer divisible by both inputs.

    Args:
        n (int): First positive integer.
        m (int): Second positive integer.

    Returns:
        int: The least common multiple of n and m.

    Raises:
        ValueError: If either integer is not positive.
    """

    if n <= 0 or m <= 0:
        raise ValueError("n and m must be positive integers")

    return n*m // gcd(n,m)