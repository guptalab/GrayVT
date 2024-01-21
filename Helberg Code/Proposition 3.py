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

    # print(vArray, m)
    with open('propositon.txt', 'a') as f:
        codewords = pp.PrettyPrinter(indent=4, stream=f)

        delList = calculateDeletionSphere(finalList, s-1)

        sphered = {}
        qAryResidue = []
        for i in ans:
            flag = True
            listTuple = [tuple(lst) for lst in ans[i]]
            x = set(listTuple)
            for j in delList:
                listTuple = [tuple(lst) for lst in delList[j]]
                y = set(listTuple)
                if len(x.intersection(y)) > 1:
                    flag = False
                    break
            if (flag and len(ans[i]) > 1):
                # print("a = ", i, file=f)
                qAryResidue.append(i)
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
                    if i not in sphered:
                        sphered[i] = []
                    sphered[i].append(code)
                    # print("original= {} <br> gray mapped= {}".format(
                    #     k, code), file=f)

        print("N = {}, q = {}, s = {}, Codeword total = {}, Max number of codewords = {}".format(
            length, numAlphabets, s, len(finalList), max(len(v) for v in ans.values())), file=f)

        # print("{} {}".format(m, vArray), file=f)
        list = []
        maxi = 0
        for i in sphered:
            maxi = max(maxi, len(sphered[i]))

        for i in sphered:
            if (len(sphered[i]) >= maxi):
                list.append((i, len(sphered[i])))
        list.sort(key=lambda x: x[1], reverse=True)
        # print(list)
        print(list, file=f)

        binaryResidue = []
        error = 0
        for j in sphered:
            if (len(sphered[j]) > 1):
                # print("a = ", j, file=f)
                # print(sphered[j], file=f)
                delList = calculateDeletionSphere(sphered[j], s)
                binaryResidue.append(j)

                reverseDelList = {}
                for i in delList:
                    for k in delList[i]:
                        if tuple(k) not in reverseDelList:
                            reverseDelList[tuple(k)] = []
                        reverseDelList[tuple(k)].append(i)
                delList = reverseDelList
                # print("deletion sphere", file=f)
                # codewords.pprint(delList)

                flag = True
                for i in delList:
                    listTuple = [tuple(lst) for lst in delList[i]]
                    x = set(listTuple)
                    for w in delList:
                        listTuple = [tuple(lst) for lst in delList[w]]
                        y = set(listTuple)
                        if len(x.intersection(y)) == 0 or x == y:
                            flag = True
                        else:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    code = []
                    for i in delList:
                        code.append(i)
                    # print("--------------No intersection------------<br>",
                    #       code, file=f)
                else:
                    error += 1
                    print(j, len(sphered[j]), "intersecting")

        print("Error = ", error, file=f)
        # print(len(qAryResidue), sorted(qAryResidue), file=f)
        # print(sorted(binaryResidue), file=f)

        print("============================================================================\n\n\n", file=f)
