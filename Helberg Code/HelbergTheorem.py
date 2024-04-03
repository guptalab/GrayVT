# Author: Devdeep.js
# Date: 2024-01-05
# Description: Analysis functions for Helberg's theorem.

import numpy as np
import pprint as pp
from helbergUtility import HelbergUtility

def analyzeTheorem1(n, q, s):
    helbergUtility = HelbergUtility()
    string = []
    finalList = []
    vArray = np.zeros(n)
    ans = {}

    if s < n:
        helbergUtility.generateStrings(n, q, string, finalList)
        string = finalList
        string = np.array(string)
        helbergUtility.generateVArray(n, s, vArray, q)
        m = helbergUtility.calculateM(vArray, s, n, q)
        for i in string:
            helbergUtility.calculateMoment(i, vArray, m, n, ans)
    else:
        ans[0] = []
        exit("s should be less than n")

    qry = {}
    with open('temp.csv', 'a') as f:
        print("For q = ", q, "n = ", n,
              "Weights and m :", vArray, m, file=f)
        codewords = pp.PrettyPrinter(indent=4, stream=f)
        for i in ans:
            if len(ans[i]) > 1:
                # print("a = ", i, file=f)
                for k in ans[i]:
                    code = []
                    for j in k:
                        if j == 0:
                            code.append(1)
                            code.append(1)
                        elif j == 1:
                            code.append(0)
                            code.append(1)
                        elif j == 2:
                            code.append(1)
                            code.append(0)
                        else:
                            code.append(0)
                            code.append(0)
                    if (i, tuple(k)) not in qry:
                        qry[(i, tuple(k))] = tuple(code)

        sorted(qry)
        # print(codewords.pprint(qry), file=f)
        print("For Queterenary: ", file=f)
        print("N = {}, q = {}, s = {}, Codeword total = {}, Max number of codewords = {}".format(
            n, q, s, len(finalList), max(len(v) for v in ans.values())), file=f)
        print("============================================================================", file=f)

        list_ = []
        maxi = 0
        for i in ans:
            maxi = max(maxi, len(ans[i]))

        for i in ans:
            if len(ans[i]) >= maxi:
                list_.append((i))
        list_.sort()
        print(list_)
        ans = {}
        binary = {}
        string = []
        finalList = []
        vArray = np.zeros(2*n)
        if s < n:
            helbergUtility.generateStrings(2*n, q-2, string, finalList)
            string = finalList
            string = np.array(string)
            helbergUtility.generateVArray(2*n, s+1, vArray, q-2)
            m = helbergUtility.calculateM(vArray, s+1, 2*n, q-2)
            for i in string:
                helbergUtility.calculateMoment(i, vArray, m, 2*n, ans)

        print("For q = ", q-2, "n = ", 2*n,
              "Weights and m :", vArray, m, file=f)
        for i in ans:
            if len(ans[i]) > 1:
                for k in ans[i]:
                    code = []
                    for j in range(0, len(k), 2):
                        if k[j] == 0 and k[j+1] == 1:
                            code.append(1)
                        if k[j] == 0 and k[j+1] == 0:
                            code.append(3)
                        if k[j] == 1 and k[j+1] == 1:
                            code.append(0)
                        if k[j] == 1 and k[j+1] == 0:
                            code.append(2)
                    if (i, tuple(k)) not in qry:
                        binary[(i, tuple(k))] = tuple(code)

        sorted(binary)
        # print(codewords.pprint(binary), file=f)

        print("For Binary: ", file=f)
        print("N = {}, q = {}, s = {}, Codeword total = {}, Max number of codewords = {}".format(
            2*n, q-2, s+1, len(finalList), max(len(v) for v in ans.values())), file=f)
        print("============================================================================", file=f)

        # Connect the dictionaries
        for key1, value1 in qry.items():
            for key2, value2 in binary.items():
                if value1 == key2[1] and key1[0] in list_:
                    print(
                        f"a = {key1[0]} , a' = {key2[0]}, {key1[1]} = {value1} qary --> binary {key2[1]} in {value2}", file=f)
        print("============================================================================\n\n\n\n\n", file=f)
