# def counting_sort(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)

#     for num in arr:
#         count[num] += 1

#     for i in range(1, len(count)):
#         count[i] += count[i - 1]

#     output = [0] * len(arr)

#     for num in arr:
#         output[count[num] - 1] = num
#         count[num] -= 1
        
#     for i in range(len(arr)):
#         arr[i] = output[i]


# array = [4, 2, 2, 8, 3, 3, 1]
# sorted_array = counting_sort(array)
# print("Sorted array:", array)


def counting_sort(arr):
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Create a count array with size based on the range of values in arr
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements

    # Count occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Modify count array to store the cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create output array
    output = [0] * len(arr)

    # Place elements into output array in sorted order
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    # Copy sorted elements back into the original array
    for i in range(len(arr)):
        arr[i] = output[i]

# Example usage
array = [4, -2, 2, -8, 3, 3, 1]
counting_sort(array)
print("Sorted array:", array)

