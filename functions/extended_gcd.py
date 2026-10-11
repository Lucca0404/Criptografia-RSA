def extended_gcd_iterative_2(n : int, m : int) -> tuple[int,int,int]:
    """
    Compute the GCD and Bézout coefficients of two positive integers.

    Use the iterative Extended Euclidean Algorithm to find integers
    x and y such that n*x + m*y = gcd(n, m).

    Args:
        n (int): First positive integer.
        m (int): Second positive integer.

    Returns:
        tuple[int, int, int]: The GCD of n and m, followed by
            the Bézout coefficients x and y, respectively.

    Raises:
        ValueError: If either integer is not positive.
    """

    if m <= 0 or n <= 0:
        raise ValueError("n and m must be positive integers")
    
    if n % m == 0:
        return (m,0,1)
    
    x = [0, 1]
    y = [1, (-1) * (n // m)]

    while m != 0:
        r = n % m
        n = m
        m = r
        if m != 0 and n % m != 0:
            x.append((-1) * (n // m) * x[-1] + (x[-2])) 
            y.append((-1) * (n // m) * y[-1] + (y[-2])) 

    return (n,x[-1],y[-1])

def extended_gcd_recursive(a: int, b: int) -> tuple[int, int, int]:
    """
    Compute the GCD and Bézout coefficients of two integers
    using the recursive Extended Euclidean Algorithm.

    Return (gcd, x, y) such that a*x + b*y = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0

    d, x1, y1 = extended_gcd_recursive(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return d, x, y

def extended_gcd_iterative(a: int, b: int) -> tuple[int, int, int]:
    """
    Compute the GCD and Bézout coefficients using the
    iterative Extended Euclidean Algorithm.
    """
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1

    while r != 0:
        q = old_r // r

        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y

    return old_r, old_x, old_y