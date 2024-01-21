import numpy as np
import pprint as pp
import sys
import collections


def generateStrings(length, numAlphabets, string, finalList):
    if length == 0:
        finalList.append(string[:])
    else:
        for j in range(0, numAlphabets):
            string.append(j)
            generateStrings(length-1, numAlphabets, string, finalList)
            string.pop()
    return string


def generateVArray(length, s, vArray, numAlphabets):
    for i in range(0, length):
        for j in range(1, s+1):
            vArray[i] += vArray[i-j] if (i-j >= 0) else 0
        vArray[i] = vArray[i]*(numAlphabets-1) + 1


def calculateM(vArray, s, length, numAlphabets):
    m = 0
    for i in range(1, s+1):
        m += vArray[length-i]
    return m*(numAlphabets-1) + 1


def calculateMoment(num, vArray, m, length, ans):
    sum = 0
    for i in range(0, length):
        sum += vArray[i]*num[i]
    sum = sum % m
    if sum not in ans:
        ans[sum] = []
    ans[sum].append(num)


def calculateDeletionSphere(finalList, num):
    tempList = []
    delList = {}
    for i in finalList:
        for j in range(len(i)):
            pref = i[:j]
            suff = i[j+1:]
            temp = tuple(pref) + tuple(suff)
            if (num > 0) and (temp not in tempList):
                tempList.append(temp)
            else:
                if temp not in delList:
                    delList[temp] = []
                if i not in delList[temp]:
                    delList[temp].append(i)
    mainList = {}
    if (num <= 0):
        return delList
    else:
        num -= 1
        x = calculateDeletionSphere(tempList, num)
        newDict = {}
        for i in x:
            for j in x[i]:
                if (j in delList):
                    tuple1 = tuple(i for i in delList[j])
                    for k in delList[j]:
                        if i not in newDict:
                            newDict[i] = []
                        if k not in newDict[i]:
                            newDict[i].append(k)
        return newDict


if __name__ == "__main__":
    string = []
    finalList = []
    if len(sys.argv) != 4:
        print("Usage: python3 helberg.py n q s")
        sys.exit()

    length = int(sys.argv[1])
    numAlphabets = int(sys.argv[2])
    s = int(sys.argv[3])
    vArray = np.zeros(length)
    ans = {}

    if s < length:
        generateStrings(length, numAlphabets, string, finalList)
        string = finalList
        string = np.array(string)
        generateVArray(length, s, vArray, numAlphabets)
        m = calculateM(vArray, s, length, numAlphabets)
        for i in string:
            calculateMoment(i, vArray, m, length, ans)

    else:
        ans[0] = []
        exit("s should be less than n")

    qry = {}
    with open('data_gen.txt', 'a') as f:
        print("For q = ", numAlphabets, "n = ", length,
              "Weights and m :", vArray, m, file=f)
        codewords = pp.PrettyPrinter(indent=4, stream=f)
        for i in ans:
            if (len(ans[i]) > 1):
                # print("a = ", i, file=f)
                for k in ans[i]:
                    code = []
                    for j in k:
                        if (j == 0):
                            code.append(1)
                            code.append(1)
                        elif (j == 1):
                            code.append(0)
                            code.append(1)
                        elif (j == 2):
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
            length, numAlphabets, s, len(finalList), max(len(v) for v in ans.values())), file=f)
        print("============================================================================", file=f)

        list = []
        maxi = 0
        for i in ans:
            maxi = max(maxi, len(ans[i]))

        for i in ans:
            if (len(ans[i]) >= maxi):
                list.append((i))
        list.sort()
        print(list)
        ans = {}
        binary = {}
        string = []
        finalList = []
        vArray = np.zeros(2*length)
        if s < length:
            generateStrings(2*length, numAlphabets-2, string, finalList)
            string = finalList
            string = np.array(string)
            generateVArray(2*length, s+1, vArray, numAlphabets-2)
            m = calculateM(vArray, s+1, 2*length, numAlphabets-2)
            for i in string:
                calculateMoment(i, vArray, m, 2*length, ans)

        print("For q = ", numAlphabets-2, "n = ", 2*length,
              "Weights and m :", vArray, m, file=f)
        for i in ans:
            if (len(ans[i]) > 1):
                for k in ans[i]:
                    code = []
                    for j in range(0, len(k), 2):
                        if (k[j] == 0 and k[j+1] == 1):
                            code.append(1)
                        if (k[j] == 0 and k[j+1] == 0):
                            code.append(3)
                        if (k[j] == 1 and k[j+1] == 1):
                            code.append(0)
                        if (k[j] == 1 and k[j+1] == 0):
                            code.append(2)
                    if (i, tuple(k)) not in qry:
                        binary[(i, tuple(k))] = tuple(code)

        sorted(binary)
        # print(codewords.pprint(binary), file=f)

        print("For Binary: ", file=f)
        print("N = {}, q = {}, s = {}, Codeword total = {}, Max number of codewords = {}".format(
            2*length, numAlphabets-2, s+1, len(finalList), max(len(v) for v in ans.values())), file=f)
        print("============================================================================", file=f)

        # Connect the dictionaries
        for key1, value1 in qry.items():
            for key2, value2 in binary.items():
                # print(value1, value2, key1, key2)
                if value1 == key2[1] and key1[0] in list:
                    print(
                        f"a = {key1[0]} , a' = {key2[0]}, {key1[1]} = {value1} qary --> binary {key2[1]} in {value2}", file=f)
        print("============================================================================\n\n\n\n\n", file=f)
