arr = [10, 20, 30]
# arr.append(40)
# arr.insert(1, 15)
# arr.pop()
# arr.pop(2)
# arr.remove(15)
# print(arr)

# find number in an array
target = 10
for i in range(len(arr)):
    if arr[i] == target:
        print("found")
    else:
        print("not found")
    break 