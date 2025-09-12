#Program: Find the second largest number in a list

def second_largest(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num!=largest:
            second = num
    return second



n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))


print("Second largest:", second_largest(arr))
