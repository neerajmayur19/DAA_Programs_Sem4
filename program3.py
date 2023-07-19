#Element uniqueness problem
#In this program, the elements are added into a list and set one by one and at the end, we compare the length of the list and the set and if its equal, then it means that list contains all
#unique elements and only if the length is different, then it means the list does not contain any unique elements
n = int(input("Enter the number of the elements in the array"))
lst = []
s = set()
for i in range(n):
    element = int(input("Enter the element"))
    lst.append(element)
    s.add(element)
if len(s)==len(lst):
    print("Unique elements are present in the list")
else:
    print("The List does not contain unique elements")
  #Time complexity is O(n) in best, worst and average case 
