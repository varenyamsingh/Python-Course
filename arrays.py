arr = [10, 20, 30, 40, 50]
print(arr)
print(arr[2])
print(arr[-1]) #negative indexing means from end 
arr[1] = 99 #Changing Elements
print(arr)
print(len(arr)) #length of array

#------------------------------------------------

# Traversing an Array: means Visit every element.
#Method 1: Using for loop
for i in arr: # in this we get values directly
    print(i)

#Method 2: Using Using indexes
arr1 = [11, 12, 13, 14, 15]  # in this we get indexes then values
for i in range(len(arr1)):
    print(arr1[i])

# adding an element in an array
arr2 = [100,200,300]
arr2.append(400) # adding an element at the end of array
print(arr2)
arr2.insert(2,30) # insert anywhere in the array
print(arr2)
arr2.pop() # remove last element from the array
arr2.pop(2) # remove specific element at index 2
arr2.remove(300) # remove specific element by value
print(arr2)



arr3 = [21, 31, 41, 51, 61]
print(sum(arr3)) # sum of all elements in the array
print(max(arr3)) # maximum element in the array
print(min(arr3)) # minimum element in the array
arr3.sort(reverse=True) # sort the array in descending order
print(arr3)
print(8 in arr3) # check if 8 is present in the array or not


# find largest and smallest element in an array
arr4 = [1, 2, 3, 4, 5]
largest = [arr4[0]]
smallest = [arr4[0]]
for i in arr4:
    if i > largest[0]:
        largest[0] = i
    if i < smallest[0]:
        smallest[0] = i
print("Largest element is:", largest[0])
print("Smallest element is:", smallest[0])

