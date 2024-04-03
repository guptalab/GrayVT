import numpy as np
import collections

# Author: Devdeep.js
# Date: 2024-01-05
# Description: Utility class containing common functions for Helberg theorem calculations.


class HelbergUtility:
    @staticmethod
    def generateStrings(length, numAlphabets):
        """
        Generate all possible strings of given length and alphabet size recursively.

        Args:
        - length (int): Length of strings to generate.
        - numAlphabets (int): Number of alphabets in the alphabet set.

        Returns:
        - list: List containing all generated strings.
        """
        finalList = []

        def generate(string):
            if len(string) == length:
                finalList.append(string[:])
            else:
                for j in range(numAlphabets):
                    string.append(j)
                    generate(string)
                    string.pop()

        generate([])
        return finalList

    @staticmethod
    def generateVArray(length, s, numAlphabets):
        """
        Generate the V array required for calculations.

        Args:
        - length (int): Length of the string.
        - s (int): Parameter for calculations.
        - numAlphabets (int): Number of alphabets in the alphabet set.

        Returns:
        - numpy.ndarray: Array containing the calculated values.
        """
        vArray = np.zeros(length)
        for i in range(length):
            for j in range(1, s+1):
                vArray[i] += vArray[i-j] if (i-j >= 0) else 0
            vArray[i] = vArray[i] * (numAlphabets - 1) + 1
        return vArray

    @staticmethod
    def calculateMoment(num, vArray, m):
        """
        Calculate the moment for a given number.

        Args:
        - num (list): List representing a number.
        - vArray (numpy.ndarray): Array containing pre-calculated values.
        - m (int): Value of m for calculations.

        Returns:
        - int: Calculated moment value.
        """
        total = sum(vArray[i] * num[i] for i in range(len(num)))
        return total % m

    @staticmethod
    def calculateDeletionSphere(finalList, num):
        """
        Calculate the deletion sphere for a given list of strings.

        Args:
        - finalList (list): List of strings.
        - num (int): Parameter for deletion sphere calculations.

        Returns:
        - dict: Dictionary representing the deletion sphere.
        """
        def generateDeletionSphere(tempList, num):
            if num <= 0:
                return collections.defaultdict(list)
            num -= 1
            delList = collections.defaultdict(list)
            for i in tempList:
                for j in range(len(i)):
                    pref = i[:j]
                    suff = i[j+1:]
                    temp = tuple(pref) + tuple(suff)
                    delList[temp].append(i)
            tempDelList = generateDeletionSphere(delList.keys(), num)
            newDict = collections.defaultdict(list)
            for i in tempDelList:
                for j in tempDelList[i]:
                    if j in delList:
                        newKey = tuple(x for x in delList[j])
                        newDict[newKey].append(j)
            return newDict

        return generateDeletionSphere(finalList, num)
