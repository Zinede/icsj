import random
import time

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# Generate a list of 1000 random integers between 999 and 9999
nums = [random.randint(999, 9999) for _ in range(1000)]

# Prompt the user to enter a target integer
target = int(input("Enter the target integer: "))

# Perform linear search on the list and measure the time taken
start = time.process_time()
result = linear_search(nums, target)
end = time.process_time()

# Print the result and time taken
if result == -1:
    print("Target integer not found in the list.")
else:
    print(f"Target integer found at index {result}.")
print(f"Time taken: {end - start} seconds.")


import random
import time

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Generate a list of 1000 random integers between 999 and 9999
nums = [random.randint(999, 9999) for _ in range(1000)]

# Sort the list for binary search
nums_sorted = sorted(nums)

# Prompt the user to enter a target integer
target = int(input("Enter the target integer: "))

# Perform binary search on the unsorted list and measure the time taken
start = time.process_time()
result_unsorted = binary_search(nums, target)
end = time.process_time()

# Perform binary search on the sorted list and measure the time taken
start_sorted = time.process_time()
result_sorted = binary_search(nums_sorted, target)
end_sorted = time.process_time()

# Print the results and time taken
if result_unsorted == -1:
    print("Target integer not found in the unsorted list.")
else:
    print(f"Target integer found at index {result_unsorted} in the unsorted list.")
print(f"Time taken for unsorted list: {end - start} seconds.")

if result_sorted == -1:
    print("Target integer not found in the sorted list.")
else:
    print(f"Target integer found at index {result_sorted} in the sorted list.")
print(f"Time taken for sorted list: {end_sorted - start_sorted} seconds.")

import random

# Generate a list of 1000 random integers between -5000 and 5000
nums = [random.randint(-5000, 5000) for _ in range(1000)]

def count_negatives(nums):
    negative_count = 0
    for num in nums:
        if num < 0:
            negative_count += 1
    negative_percentage = (negative_count / len(nums)) * 100
    return [negative_count, negative_percentage]

# Example usage
nums = [random.randint(-5000, 5000) for _ in range(1000)]
neg_count, neg_percentage = count_negatives(nums)
print(f"Number of negative numbers: {neg_count}")
print(f"Percentage of negative numbers: {neg_percentage:.2f}%")

def count_zeros_and_digits(nums):
    zero_count = 0
    digit_count = 0
    for num in nums:
        digit_count += len(str(abs(num)))
        if num == 0:
            zero_count += 1
    return [zero_count, digit_count]

# Example usage
nums = [random.randint(-5000, 5000) for _ in range(1000)]
zero_count, digit_count = count_zeros_and_digits(nums)
print(f"Number of zeros: {zero_count}")
print(f"Total number of digits: {digit_count}")

import random
import time

def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid-1, x)
        else:
            return binary_search_recursive(arr, mid+1, high, x)
    else:
        return -1

def binary_search_while(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def binary_search_for(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        elif arr[i] > x:
            break
    return -1

# Test the functions
random.seed(0)
arr = sorted(random.sample(range(10000), 1000))
x = random.randint(0, 9999)

start_time = time.time()
binary_search_recursive(arr, 0, len(arr)-1, x)
print(f"Time taken by binary_search_recursive: {time.time() - start_time}")

start_time = time.time()
binary_search_while(arr, x)
print(f"Time taken by binary_search_while: {time.time() - start_time}")

start_time = time.time()
binary_search_for(arr, x)
print(f"Time taken by binary_search_for: {time.time() - start_time}")
