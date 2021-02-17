def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    arr = []

    # O(n^2) traverse through the 4x4 matrix and construct the array.
    for i in range(0, len(matrix)):
        m = matrix[i]
        for j in range(0, len(m)):
            arr.append(m[j])
    return arr

def pro_matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array. (Robin Jadoul) """
    return bytes(sum(matrix, []))

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

# Testing out the nature of the function
print(bytes2matrix([1, 2, 3, 4, 5, 6, 7, 8]))

# Retrieve flag with own implementation
flag = matrix2bytes(matrix)
print("".join([chr(f) for f in flag]))

# Retrieve flag with pro implementation
flag = pro_matrix2bytes(matrix)
print(flag.decode("utf-8"))