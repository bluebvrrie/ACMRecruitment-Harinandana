def rotate_and_convert(binary_str, k):
    n = len(binary_str)
    k = k % n  # normalize k so it's within the string length
    
    # Rotate right by k steps
    if k:
        rotated = binary_str[-k:] + binary_str[:-k]
    else:
        rotated = binary_str
    # Convert rotated binary string to decimal
    return int(rotated, 2)

# Example usage
print(rotate_and_convert("1011", 1))  
print(rotate_and_convert("1011", 2))  
print(rotate_and_convert("1011", -1)) 
print(rotate_and_convert("0010", -1))
