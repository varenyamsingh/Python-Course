arr = [10, 20, 30, 40, 50]
# arr.append(40)
# arr.insert(1, 15)
# arr.pop()
# arr.pop(2)
# arr.remove(15)
# print(arr)

# find number in an array
# target = 10
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found")
#     else:
#         print("not found")
#     break 


# for interviews using return
# 1st method
# def linear_search(arr, target):
#     for num in arr:
#         if num == target:
#             return True
#     return False

# 2nd method
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# --------------------------------------------------

# finding the largest number
# largest = arr[0]
# for i in range(len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]
# print("largest number is:", largest)

# ---------------------------------------------------

# count even numbers
# even_count = 0
# for num in arr:
#     if num % 2 == 0:
#         even_count += 1
# print("count of even numbers is:", even_count)

# ----------------------------------------------------

# Sum and Average of an array
# total_sum = 0
# for num in arr:
#     total_sum += num # sum of an array
#     average = total_sum / len(arr) # average of an array
# print("sum of array is:", total_sum)
# print("average of array is:", average)

# -----------------------------------------------------

# Reverse an array
# arr.reverse()
# arr[::-1]
# print(arr)

# Use two pointers.
left = 0
right = len(arr) - 1

while left < right:
    arr[left],arr[right]=arr[right],arr[left]
    left += 1
    right -= 1
print(arr)
