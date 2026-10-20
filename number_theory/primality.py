from math import isqrt

def is_prime_traditional(n: int) -> bool:
    """
    Determine whether an integer is prime using trial division.

    Check all possible divisors from 2 up to the integer
    square root of n.

    Args:
        n (int): Integer to be tested for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False

    return True


def is_prime_odd(n: int) -> bool:
    """
    Determine whether an integer is prime by testing odd divisors.

    Handle even integers separately, then check only odd
    divisors up to the square root of n.

    Args:
        n (int): Integer to be tested for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


def is_prime_6k(n: int) -> bool:
    """
    Determine whether an integer is prime using the 6k ± 1 rule.

    Handle divisibility by 2 and 3 separately, then test
    candidates of the form 6k - 1 and 6k + 1.

    Args:
        n (int): Integer to be tested for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6

    return True



def is_prime(n : int) -> bool:

    if n <= 1:
        return False

    if n in (2,3):
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    p = 5
    while p * p <= n:
        if n % p == 0 or n % p + 2 == 0:
            return False
        p += 6

    return True