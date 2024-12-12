
# Part 3

import time 
import random
import pandas

# COUNTING SORT:
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)

    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1
        
    for i in range(len(arr)):
        arr[i] = output[i]


# RADIX SORT:
def counting_sort_by_digit(array, digit_position):

    count = [0] * 10
    output = [0] * len(array)
    
    for num in array:
        digit = (num // 10**digit_position) % 10
        count[digit] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for i in range(len(array) - 1, -1, -1):
        digit = (array[i] // 10**digit_position) % 10
        output[count[digit] - 1] = array[i]
        count[digit] -= 1
    
    for i in range(len(array)):
        array[i] = output[i]


def radix_sort(array):

    max_value = max(array)
    num_digits = len(str(max_value))


    for digit_position in range(num_digits):
        counting_sort_by_digit(array, digit_position)

    return array

# BUCKET SORT:
def bucket_sort(array):
    n = len(array)
    buckets = [[] for _ in range(10)]
    for i in range(n):
        index = int(array[i] * 10) 
        buckets[index].append(array[i])
    for bucket in buckets:
        InsertionSort1(bucket)
    result = []
    for bucket in buckets:
        result.extend(bucket) 
    return result



array = [random.randint(0,1000) for x in range (0,300)]
start_time = time.time()
sorted_array = counting_sort(array)
end_time = time.time()
print("Sorted array is: ", array)
print("Time taken by counting sort is: ", end_time - start_time, "seconds")
start_time2 = time.time()
bucket_sort(array)
end_time2= time.time()
print("Time taken by Bucket sort is: ", end_time2 - start_time2, "seconds")
start_time3 = time.time()
radix_sort(array)
end_time3 = time.time()
print("Time taken by Radix sort is: ", end_time3 - start_time3, "seconds")

