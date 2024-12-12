# from funcs import InsertionSort1
# from funcs import RandomArray
# import math

# def bucket_sort(array):
#     n = len(array)
#     buckets = [[] for _ in range(10)]
#     for i in range(n):
#         index = int(array[i] * 10) 
#         buckets[index].append(array[i])
#     for bucket in buckets:
#         InsertionSort1(bucket)
#     result = []
#     for bucket in buckets:
#         result.extend(bucket) 
#     return result


# # Example usage
# array = [0.78, 0.17, 0.39, 0.72, 0.94, 0.21, 0.12, 0.23,0.34, 0.68]
# sorted_array = bucket_sort(array)
# print("Sorted array:", sorted_array)
# print(len(array))

from funcs import InsertionSort1
from funcs import RandomArray
import math

def bucket_sort(array):
    n = len(array)
    if n == 0:
        return []

    # Find minimum and maximum values in the array
    min_val = min(array)
    max_val = max(array)

    # Calculate the range of elements
    range_val = max_val - min_val

    # Create buckets based on the number of elements
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements into buckets
    for num in array:
        # Calculate bucket index for both decimals and whole numbers
        index = int((num - min_val) / range_val * (bucket_count - 1))
        buckets[index].append(num)

    # Sort each bucket and merge them
    result = []
    for bucket in buckets:
        InsertionSort1(bucket)  # Using insertion sort on each bucket
        result.extend(bucket)   # Extend sorted bucket to the result

    return result

# Example usage with both decimal and whole numbers
array = [0.78, 0.17, 0.39, 0.72, 0.94, 0.21, 0.12, 0.23, 0.34, 0.68, 70, 5, 3, 9, -4, 1, 699]
sorted_array = bucket_sort(array)
print("Sorted array:", sorted_array)


