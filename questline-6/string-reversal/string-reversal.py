print("iterative method")
a=input("enter a string ")
r=""
for ch in a:
    r=ch+r
print("reversed string is",r)

print("\nrecursive method")
def rev(b):
    if b=="" or len(b)==1:
        return b
    return rev(b[1:])+b[0]
print (rev(input("enter a string")))
