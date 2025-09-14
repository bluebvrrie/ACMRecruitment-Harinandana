num=list(map(int,input("enter no:s with space in btw ").split()))
n=len(num)
for i in range(n):
    for j in range(0,n-i-1):
        if num[j] > num[j+1]:
            a= num[j]
            num[j]= num[j+1]
            num[j+1]= a
print("Sorted array:",num)
                
