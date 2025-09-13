while True:
    a=int(input("enter a no:"))
    b=bin(a)[2:]
    if b==b[::-1]:
        print("binary of",a,"is palindrome")
    else:
        print("binary of",a,"is not palindrome")
