v = [1, 4, 13, 40, 121, 364]

s = [(0, 0, 0, 0, 0, 1), (0, 1, 1, 0, 0, 0), (1, 1, 1, 0, 1, 0)]
sum = []
for j in range(len(s)):
    temp = 0
    for i in range(len(v)):
        temp += v[i]*s[j][i]
    temp = temp % 1093
    sum.append(temp)

print(sum)
