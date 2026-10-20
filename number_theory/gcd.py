def gcd(n: int, m: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two
    non-negative integers using the Euclidean algorithm.

    Return 0 if both integers are zero.

    Raise ValueError if either integer is negative.
    """
    if n < 0 or m < 0:
        raise ValueError("n and m must be non-negative integers")

    while m != 0:
        r = n % m
        n = m
        m = r

    return n
