l=list(map(int,input("Enter the array elements :").split()))
f=s=0
for i in range(len(l)):
    if l[i]>f:
        s=f
        f=l[i]
    elif l[i]>s:
        s=l[i]
for i in range(len(l)):
    if l[i]<s:
        print(l[i],end=" ")
