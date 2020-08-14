l=list(map(int,input("Enter the array elements :").split()))
l.sort()
for i in range(1,len(l)-1,2):
    l[i],l[i+1]=l[i+1],l[i]
print(*l)