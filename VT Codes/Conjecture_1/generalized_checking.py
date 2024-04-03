def generate_all_binary_sequences(n):
    def generate_sequences_helper(prefix, remaining_bits):
        if remaining_bits == 0:
            sequences.append(prefix)
            return
        generate_sequences_helper(prefix + '0', remaining_bits - 1)
        generate_sequences_helper(prefix + '1', remaining_bits - 1)
    
    sequences = []
    generate_sequences_helper('', 2 * n)
    return sequences

def find_a_b(x):
    n = len(x) // 2
    a = 0
    for i in range(n - 1):
        x1 = int(x[2*i]) 
        x2 = int(x[2*i + 1])
        x3 = int(x[2*i + 2]) 
        x4 = int(x[2*i + 3]) 
        a += ((i+1) * (1 - x1 - x2 + x2*(x1+x3+x4) + x1*x3 - x1*x3*(x2+x4) - x2*x4*(x1+x3) + 2*x1*x2*x3*x4))
        a = a % n
    
    b = 0
    for i in range(n):
        x1 = int(x[2*i]) 
        x2 = int(x[2*i + 1])
        b += (3*x1 + x2 - 2*x1*x2)
        b = b % 4
    
    return a, b

# Iterate over n from 1 to 10

with open("Results.txt", "w") as file:
    pass
for n in range(1, 11):
    print(f"For n = {n}:\n")
    
    # Open or create a file for appending
    with open("Results.txt", "a") as file:
        # Generate all possible binary sequences of length 2n
        sequences = generate_all_binary_sequences(n)

        # Write separator for new n value
        file.write(f"{'='*40}\n")
        file.write(f"For n = {n}:\n")
        file.write(f"{'='*40}\n")

        # Iterate over all sequences
        errors_found = False
        for x in sequences:
            for i in range(len(x)):
                if x[i] == '1':
                    # Remove '1' at the delete index
                    x_del = x[:i] + x[i+1:]

                    # Choose a random index to insert '0'
                    for j in range(len(x_del) + 1):
                        y = x_del[:j] + '0' + x_del[j:]

                        # Calculate a and b for x and y
                        a_x, b_x = find_a_b(x)
                        a_y, b_y = find_a_b(y)

                        # Calculate absolute differences
                        abs_diff_a = abs(a_x - a_y)
                        abs_diff_b = abs(b_x - b_y)

                        # Check if both abs_diff_a and abs_diff_b are zero
                        if abs_diff_a == 0 and abs_diff_b == 0:
                            # Write the results to the file
                            file.write(f"x: {x}\n")
                            file.write(f"y: {y}\n")
                            file.write(f"|a_x - a_y|: {abs_diff_a}\n")
                            file.write(f"|b_x - b_y|: {abs_diff_b}\n")
                            file.write("=" * 40 + "\n")
                            errors_found = True

        # If no errors found, write a message
        if not errors_found:
            file.write(f"No error found for n = {n}\n")
