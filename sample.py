import sys
def maximizeExpression(A):
 
    # input should have at least 4 elements
    if len(A) < 4:
        exit(-1)
 
    # create 4 lookup tables and initialize them to -sys.maxsize
    first = [-sys.maxsize] * (len(A) + 1)
    second = [-sys.maxsize] * len(A)
    third = [-sys.maxsize] * (len(A) - 1)
    fourth = [-sys.maxsize] * (len(A) - 2)
 
    # first stores the maximum value of A[l]
    for i in reversed(range(len(A))):
        first[i] = max(first[i + 1], A[i])
 
    # second stores the maximum value of A[l] - A[k]
    for i in reversed(range(len(A) - 1)):
        second[i] = max(second[i + 1], first[i + 1] - A[i])
 
    # third stores the maximum value of A[l] - A[k] + A[j]
    for i in reversed(range(len(A) - 2)):
        third[i] = max(third[i + 1], second[i + 1] + A[i])
 
    # fourth stores the maximum value of A[l] - A[k] + A[j] - A[i]
    for i in reversed(range(len(A) - 3)):
        fourth[i] = max(fourth[i + 1], third[i + 1] - A[i])
 
    # maximum value would be present at fourth[0]
    return fourth[0]



def read_input_from_file(filename):
    with open(filename, 'r') as file:
        # Read the total number of elements from the first line
        total_elements = int(file.readline().strip())
        
        # Initialize an empty list to store elements
        elements = []
        
        # Read the elements in chunks
        chunk_size = 10000  # Adjust the chunk size as needed
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file
            elements.extend(map(int, chunk.split()))
    return total_elements, elements
# Example usage: Read input from a text file named "input.txt"
total_elements, elements = read_input_from_file("testcase8.txt")
print(maximizeExpression(elements))

