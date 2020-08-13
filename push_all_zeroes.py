l=list(map(int,input("Enter the array elements : ").split()))
s=0
for i in range(len(l)):
    if l[i]==0:
        continue
    l[s],l[i]=l[i],l[s]
    s+=1
while(s<len(l)):
    l[s]=0
    s+=1
print(l)

#output
#Enter the array elements : 0 1 2 7 0 8 9 0 4 2
# [1, 2, 7, 8, 9, 4, 2, 0, 0, 0]
