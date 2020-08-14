l=list(map(int,input("Enter the array elements :").split()))

# Naive Solution
# A=[]
# a=l[0]*l[1]
# print(a)
# A.append(a)
# for i in range(1,len(l)-1):
#     A.append(l[i-1]*l[i+1])
# A.append(l[-1]*l[-2])
# print(A)


#Optimised solution
prev=l[0]
l[0]=l[0]*l[1]
for i in range(1,len(l)-1):
    c=l[i]
    l[i]=prev*l[i+1]
    prev=c
l[-1]=prev*l[-1]
print(l)
