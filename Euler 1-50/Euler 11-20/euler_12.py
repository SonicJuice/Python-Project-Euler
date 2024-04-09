"""
Highly Divisible Triangular Number
------------------------------------
The sequence of triangles is generated by adding the natural numbers; the first seven 
and there divisors are:
1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
Find the value of the first to have > n divisors.
"""

import math

def _divisor_count(n):
    """ memoisation caches function results to avoid repeated calls that process 
    the same input. """
    if n in memo:
        return memo[n]
    count = 0
    sqrt_n = math.isqrt(n)
    """  no prime factors of a number are > its square root """
    for i in range(1, sqrt_n + 1):
        """ and factors are paired such that each factor i of a number num has a complementary 
        factor num/i. """
        if n % i == 0:
            count += 2
    """ n is a perfect square, so ensure its sqrt is only stored once. """
    if sqrt_n * sqrt_n == n:
        count -= 1
    memo[n] = count
    return count

def highly_divisible_triangle(num):
    n = 1
    while True:
        if n % 2 == 0:
            """ divisor_count is multiplicative, so if m and n are coprime, 
            σ(mn) = σ(m) ⋅ σ(n) """
            divisors_n = _divisor_count(n // 2) * _divisor_count(n + 1)
        else:
            divisors_n = _divisor_count(n) * _divisor_count((n + 1) // 2)
        if divisors_n > num:
            """ nth triangle number. """
            return n * (n + 1) // 2
        n += 1

if __name__ == "__main__":
    memo = {}
    print(highly_divisible_triangle(500))
