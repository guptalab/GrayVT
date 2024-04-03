# Author: Devdeep.js
# Date: 2024-01-05
# Description: Python script for analyzing Helberg's Theorem 1.

import sys
from helbergAnalysis import analyzeTheorem1

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py n q s")
        sys.exit()

    n = int(sys.argv[1])
    q = int(sys.argv[2])
    s = int(sys.argv[3])

    analyzeTheorem1(n, q, s)
