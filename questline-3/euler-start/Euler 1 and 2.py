#Problem 1
N = 1000
a=3
b=5
total = 0

# Add multiples of a
for i in range(a, N, a):
    total += i

# Add multiples of b
for i in range(b, N, b):
    if i % a != 0:  #To remove no:s already added
        total += i

print("sum of all the multiples of 3 and 5 below 1000 =",total)

#Problem 2
n1=1
n2=2
total=0
x=4000000

while n1<=x:  """defines range"""
    if n1 % 2 == 0:
        total += n1  """takes sum if no: is even"""
        
    n=n1  """n1 is stored temporarily to avoid error""" 
    n1=n2
    n2=n+n2
    
print("sum of even fibonacci no: =",total)
