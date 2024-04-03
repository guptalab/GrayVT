# Author: Devdeep.js
# Date: 2024-01-05
# Description: Python script to calculate asymptotic bounds.

def calculateAsymptoticBounds(d, q, startN, endN):
    """
    Calculate asymptotic bounds for given parameters.

    Args:
    - d (int): The value of d.
    - q (int): The value of q.
    - startN (int): The starting value of n.
    - endN (int): The ending value of n.

    Returns:
    - None
    """
    for n in range(startN, endN + 1):
        lowerBound = round(d * d * pow(q, n + d) / (pow(q - 1, 2 * d) * pow(n, 2 * d)), 3)
        upperBound = round(d * pow(q, n) / (pow(q - 1, d) * pow(n, d)), 3)
        print(f"For n = {n}, lower bound = {lowerBound}, upper bound = {upperBound}")

if __name__ == "__main__":
    d = 2
    q = 2
    startN = 3
    endN = 15

    calculateAsymptoticBounds(d, q, startN, endN)
