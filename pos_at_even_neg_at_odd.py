l=list(map(int,input("Enter the array elements : ").split()))
po=0
ne=1
le=len(l)
while(True):
    while (po<le and l[po]>=0):
        po+=2
    while (ne<le and l[ne]<=0):
        ne+=2
    if (po<le and ne<le):
        l[po],l[ne]=l[ne],l[po]
    else:
        break
print(l)

