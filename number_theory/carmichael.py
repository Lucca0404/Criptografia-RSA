from number_theory.lcm import lcm


def carmichael(n: int) -> int:
    """
    Compute Carmichael's lambda function for a positive integer.

    Determine the smallest positive exponent k such that
    a**k is congruent to 1 modulo n for every integer a
    coprime to n.

    Args:
        n (int): Positive integer whose Carmichael value
            is to be computed.

    Returns:
        int: The value of Carmichael's lambda function.

    Raises:
        ValueError: If n is not a positive integer.
    """


    if n <= 0:
        raise ValueError("n must be a positive integer")


    if n == 1 or n == 2:
        return 1
    
    
    factorization = []

    p = 3

    c = 0


    while n % 2 == 0:
        n //= 2
        c += 1


    if c == 2: factorization.append(2)
        
    elif c > 2: factorization.append(2**(c-2))


    while p * p <= n:
        c = 0
        if n % p == 0:
            while n % p == 0:
                c += 1
                n //= p
            factorization.append(p**(c-1)*(p-1))
        p += 2
    if n > 1:
        factorization.append(n-1)

    
    result = 1


    for i in range(len(factorization)):
        result = lcm(result,factorization[i])


    return result