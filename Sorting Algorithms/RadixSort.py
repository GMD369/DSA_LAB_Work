# Helper function: Counting Sort by digit position
# def counting_sort_by_digit(array, digit_position):

#     count = [0] * 10
#     output = [0] * len(array)
    
#     for num in array:
#         digit = (num // 10**digit_position) % 10
#         count[digit] += 1
    
#     for i in range(1, len(count)):
#         count[i] += count[i - 1]
    
#     for i in reversed(len(array) - 1, -1, -1):
#         digit = (array[i] // 10**digit_position) % 10
#         output[count[digit] - 1] = array[i]
#         count[digit] -= 1
    
#     for i in range(len(array)):
#         array[i] = output[i]


# def radix_sort(array):

#     max_value = max(array)
#     num_digits = len(str(max_value))


#     for digit_position in range(num_digits):
#         counting_sort_by_digit(array, digit_position)

#     return array

# Example usage
# array = [170, 45, 75, 90, 802, 24, 2, 66]
# sorted_array = radix_sort(array)
# print("Sorted array:", sorted_array)

def counting_sort_by_digit(array, digit_position):
    count = [0] * 10
    output = [0] * len(array)

    # Count occurrences of each digit
    for num in array:
        digit = abs(num) // 10**digit_position % 10
        count[digit] += 1

    # Cumulative count for stable sorting
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array in reverse for stability
    for i in range(len(array) - 1, -1, -1):
        digit = abs(array[i]) // 10**digit_position % 10
        output[count[digit] - 1] = array[i]
        count[digit] -= 1

    # Copy sorted output back to original array
    for i in range(len(array)):
        array[i] = output[i]

def radix_sort(array):
    # Separate negative and positive numbers
    negatives = [num for num in array if num < 0]
    positives = [num for num in array if num >= 0]

    # Find maximum number of digits for positive and negative numbers
    max_positive = max(positives) if positives else 0
    max_negative = abs(min(negatives)) if negatives else 0
    max_digits = max(len(str(max_positive)), len(str(max_negative)))

    # Sort positives using counting sort by digit
    for digit_position in range(max_digits):
        counting_sort_by_digit(positives, digit_position)

    # Sort negatives (absolute values) and reverse
    for digit_position in range(max_digits):
        counting_sort_by_digit(negatives, digit_position)
    negatives = negatives[::-1]  # Reverse to maintain proper order

    # Combine negatives and positives
    array[:] = negatives + positives
    return array

# Example usage with negative and positive numbers
array = [170, -45, 75, -90, -802, 24, 2, 66]
sorted_array = radix_sort(array)
print("Sorted array:", sorted_array)
