def extended_gcd(n : int, m : int) -> tuple[int,int,int]:
        """
    Compute the GCD and Bézout coefficients of two integers.

    Return (gcd, x, y) such that a*x + b*y = gcd(a, b),
    using the Extended Euclidean Algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        tuple[int, int, int]: The GCD and the Bézout coefficients
            x and y, respectively.
    """
    