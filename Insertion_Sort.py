#Insertion Sort
#This sorting makes use of the method of dividing the array into unsorted and sorted in each and every step
#It shifts the element to right each time, the current element is greater than the previous element instead of swapping
#unlike the previous methods of sorting

def insertion_sort(arr):
    for i in range(len(arr)):
        current = arr[i]
        j = i - 1
        while j>=0 and arr[j]>current:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = current

arr = [2,34,90,-3,4,0]
insertion_sort(arr)
print(arr)
#In the best case it has a time complexity of O(n) and it has a time comlexity of O(n^2) in the worst case
