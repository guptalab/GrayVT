from itertools import product,permutations

def generate_combinations(n, q):
    if q <= 1:
        print("Base should be greater than 1.")
        return
    
    symbols = [str(i) for i in range(q)]
    
    combinations_list = []
    
    for combo in product(symbols, repeat=n):
        combination_str = ''.join(combo)
        combinations_list.append(combination_str)
    
    return combinations_list
def syn(x, n):
    s = 0
    count = 1
    for i in x:
        s += count * int(i)
        count += 1
    return s % (n+1)

def QaryVTCode(q,n, combinations = None):
    if combinations == None:
        combinations = generate_combinations(n, q)
    Syndrome = {}
    for i in combinations:
        s = 0
        alphax = ""
        for j in range(n-1):
            if int(i[j+1]) >= int(i[j]):
                alphax += "1" 
            else:
                alphax += "0"
            s += int(i[j])
        s += int(i[-1])
        for a in range(n):
            for b in range(q):
                if  (a,b) not in Syndrome.keys():
                        Syndrome[(a,b)] = set()
                if syn(alphax, n - 1) == a and s % q == b:
                        Syndrome[(a,b)].add(i)
    return Syndrome

def Map(x, Map):
    image = ""
    for i in x:
        image += Map[i]
    return image

def NaisargikImage(quaternaryCodebook, NaisargikMap):
    # quaternaryCodebook is a dictionary of the form {(a,b):{x1,x2,...,xn}}
    # where a is the first syndrome, b is the second syndrome, and x1,x2,...,xn are the codewords
    # for the given syndrome pair (a,b)
    # convert the codewords to Naisargik Image of length 2n.
    NaisargikImage = {}
    for syndromePair in quaternaryCodebook:
        if syndromePair not in NaisargikImage:
            NaisargikImage[syndromePair] = set()
        for codeword in quaternaryCodebook[syndromePair]:
            image = Map(codeword, NaisargikMap)
            NaisargikImage[syndromePair].add(image)    
    return NaisargikImage

def GenerateDeletionSphere(naisargikImage):
    deletionSphere = {}
    for syndromePair in naisargikImage:
        if syndromePair not in deletionSphere:
            deletionSphere[syndromePair] = {}
        for image in naisargikImage[syndromePair]:
            deletionSphere[syndromePair][image] = set()
            for i in range(len(image)):
                deletionSphere[syndromePair][image].add(image[:i]+image[i+1:])
    return deletionSphere

def countOnesAndZeros(image):
    ones = 0
    zeros = 0
    for i in image:
        if i == '1':
            ones += 1
        else:
            zeros += 1
    return ones,zeros

def checkIntersection(deletionSphere, map,n):
    with open('All_Map_Intersection'+str(n)+'.txt', 'a') as f:
        f.write("================================"+ str(map) +"==================================" + "\n")
        for syndromePair in deletionSphere:
            intersection = set()
            for image in deletionSphere[syndromePair]:
                for image2 in deletionSphere[syndromePair]:
                    if image != image2:
                        if deletionSphere[syndromePair][image] & deletionSphere[syndromePair][image2]:
                            intersection.add(image)
                            intersection.add(image2)
                            #f.write(str(syndromePair) + " " + str(image) + " " + str(image2) + "\n")
            f.write("Total number of intersecting codewords for residue "+str(syndromePair)+ " is " + str(len(intersection))+"\n")
        f.write("\n")

if __name__ == "__main__":  
    # Set of elements
    elements = ['0', '1', '2', '3']
    binary_strings = ['00', '01', '11', '10']

    # Generate permutations
    perms = permutations(binary_strings)

    # Convert permutations to a list of dictionaries
    perm_list = [dict(zip(map(str, elements), perm)) for perm in perms]

    # Print the list of dictionaries
    for idx, perm_dict in enumerate(perm_list, 1):
        print(f"{idx}. {perm_dict}")
    
    for n in range(2,10):
        quaternaryCodebook = QaryVTCode(4, n)
        for map in perm_list:
            naisargikImage = NaisargikImage(quaternaryCodebook,map)
            deletionSphere = GenerateDeletionSphere(naisargikImage)
            checkIntersection(deletionSphere, map,n)
    # for map in perm_list:
