from functions.gcd import gcd


def euler_totient_nlogn(n: int) -> int:
    """
    Compute Euler's totient function using the Euclidean algorithm.

    Count the positive integers up to n that are coprime to n
    by computing their greatest common divisor (GCD).

    The algorithm has O(n log n) time complexity and O(1)
    auxiliary space complexity.

    Args:
        n (int): A positive integer whose totient is to be computed.

    Returns:
        int : The totient value

    Raises:
        ValueError: If n is not a positive integer.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    coprimes = 1

    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes += 1

    return coprimes


def euler_totient_sqrtn(n: int) -> int:
    """
    Compute Euler's totient function using prime factorization.

    Apply Euler's product formula by identifying the distinct
    prime factors of n through trial division.

    The algorithm has O(sqrt(n)) time complexity and O(1)
    auxiliary space complexity.

    Args:
        n (int): A positive integer whose totient is to be computed.

    Returns:
        int: The number of positive integers up to n that
            are coprime to n.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    p = 2
    result = n

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p

            result -= result // p

        p += 1

    if n > 1:
        result -= result // n

    return result