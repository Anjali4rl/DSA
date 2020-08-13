def rotate_by_one(arr,n):
    s=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[i+1]=s
    return arr
l=list(map(int,input("Enter the array elements : ").split()))
arr=rotate_by_one(l,len(l))
print("The reversed array is :",arr)