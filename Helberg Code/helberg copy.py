# Helberg code
# 1. string genegration
# 2. vi array generate
# 3. find m
# 4. find a and classyfy the strings by a


# 1. string genegration
# input: n, k
# output: list of strings

import numpy as np
import pprint as pp
import sys
import collections


def String_generate(n, q, x, final_list):
    if n == 0:
        final_list.append(x[:])
    else:
        for j in range(0, q):
            x.append(j)
            String_generate(n-1, q, x, final_list)
            x.pop()
    return x


def Vi_generate(n, s, v):
    for i in range(0, n):
        for j in range(1, s+1):
            v[i] += v[i-j] if (i-j >= 0) else 0


def find_M(v, s, n):
    m = 1
    for i in range(1, s+1):
        m += v[n-i]
    return m


def func(num, v, m, n, ans):
    sum = 0
    for i in range(0, n):
        # print(v[i]*num[i])
        sum += v[i]*num[i]
    sum = sum % m
    # print(sum)
    if sum not in ans:
        ans[sum] = []
    ans[sum].append(num)


if __name__ == "__main__":
    x = []
    final_list = []
    if len(sys.argv) != 4:
        print("Usage: python3 helberg.py n q s")
        sys.exit()

    # Read the command line arguments
    n = int(sys.argv[1])
    q = int(sys.argv[2])
    s = int(sys.argv[3])
    v = np.ones(n)
    ans = {}

    if s < n:
        # Use the function
        String_generate(n, q, x, final_list)
        x = final_list
        x = np.array(x)
        # for i in x:
        #     print(i)

        Vi_generate(n, s, v)
        # print("V = ", v)

        m = find_M(v, s, n)
        # print("m = ", m)

        for i in x:
            func(i, v, m, n, ans)

    else:
        ans[0] = []
    # Open the output file
    with open('output.csv', 'a') as f:
        # Create a pretty printer object
        codewords = pp.PrettyPrinter(indent=4, stream=f)

        # Use the pretty printer to print the dictionary
        codewords.pprint(ans)

        del_list = {}
        for i in final_list:
            for j in range(len(i)):
                pref = i[:j]
                suff = i[j+1:]
                temp = str(pref+suff)
                # print(temp)
                if temp not in del_list:
                    del_list[temp] = []
                if i not in del_list[temp]:
                    del_list[temp].append(i)
        # Use the pretty printer to print the dictionary
        codewords.pprint(del_list)

        for i in ans:
            flag = True
            list_tuple = [tuple(lst) for lst in ans[i]]
            x = set(list_tuple)
            for j in del_list:
                list_tuple = [tuple(lst) for lst in del_list[j]]
                y = set(list_tuple)
                # print(x, y)
                # print(type(x), type(y), type(ans[i]), type(del_list[j]))
                if len(x.intersection(y)) > 1:
                    print(len(x.intersection(y)))
                    flag = False
                    break
            if (flag):
                print("a = ", i, file=f)
                codewords.pprint(ans[i])

        # print n , q , s and max_codeword
        print("N = ", n, ", q = ", q, ", s = ", s, ", Codeword total = ", len(final_list),
              ", Max number of codewords = ", max(len(v) for v in ans.values()), file=f)
        print(
            "============================================================================", file=f)
