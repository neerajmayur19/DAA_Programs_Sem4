#Recursive Binary Search
def binarysearch(arr,low,high,key):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binarysearch(arr,mid+1,high,key)
        else:
            return binarysearch(arr,low,mid-1,key)
    return -1
lst = [1,2,34,56,78,100]
print(binarysearch(lst,0,len(lst),3))
