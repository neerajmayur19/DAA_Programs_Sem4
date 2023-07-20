#Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr,0
    
    mid = len(arr) //2 
    left_arr,left_inversions = merge_sort(arr[:mid])
    right_arr,right_inversions = merge_sort(arr[mid:])
    merged_arr,inversions = merge(left_arr,right_arr)
    
    total = left_inversions + right_inversions + inversions
    
    return merged_arr,inversions

def merge(left,right):
    inversions = 0
    left_index = 0
    right_index = 0
    merged_arr = []
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_arr.append(left[left_index])
            left_index = left_index + 1
        else:
            merged_arr.append(right[right_index])
            inversions = inversions + (len(left)-left_index)
            right_index = right_index + 1
    merged_arr.extend(left[left_index:])
    merged_arr.extend(right[right_index:])
    
    return merged_arr,inversions
arr = [2,34,56,-9,100,9]
merged_arr, inversions = merge_sort(arr)
print(merged_arr)
print(inversions)
    
