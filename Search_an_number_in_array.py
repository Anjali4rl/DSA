def search(arr,n):
    ind=-1
    for i in range(len(arr)):
        if arr[i]==n:
            ind=i+1
            break
    return ind


l=int(input("Enter the length of arr :"))
print("Enter array element\n")
arr=list(map(int,input().split()));
n=int(input("Enter the elements to be searched:"))
ind=search(arr,n)
if ind>0:
    print("The position of ",n,"is",ind)
else:
    print("Not Found")