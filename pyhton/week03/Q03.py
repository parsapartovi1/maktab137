#3
nums = [1,2,3,9,8,7,5]
#bubble sort
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

#quick sort
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [x for x in numbers[1:] if x <= pivot]
    right = [x for x in numbers[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

#merge sort
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("Bubble:", bubble_sort(nums.copy()))
print("Quick:", quick_sort(nums.copy()))
print("Merge:", merge_sort(nums.copy()))