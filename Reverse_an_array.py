l=list(map(int,input("Enter the array elements : ").split()))
s=0
end=len(l)-1
while(s<end):
    l[s],l[end]=l[end],l[s]
    s+=1
    end-=1
print(l)