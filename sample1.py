def maximize_expression_value(A):
    n = len(A)
    max_value = float('-inf')
    for p in range(n):
        for q in range(p + 1, n):
            for r in range(q + 1, n):
                for s in range(r + 1, n):
                    expression_value = A[s] - A[r] + A[q] - A[p]
                    max_value = max(max_value, expression_value)
    return max_value
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
print(maximize_expression_value(elements))


