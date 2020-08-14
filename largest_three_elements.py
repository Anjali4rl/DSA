l=list(map(int,input("Enter the array elements :").split()))
if len(l)<3:
    print("Invalid Input")
else:
    l.sort(reverse=True)
    print(*l[:3])
