num=list(map(int,input("enter no: with sapce in btw ").split()))
print("num=",num)
k=int(input("enter a no:"))
num=num[-k:]+num[:-k]
print("rotated array is ",num)
