import time 
import random
import pandas

def Partition(array, start, end):
    p = array[start]  
    i = start + 1     
    j = end          
    while True:
        while i <= end and array[i] <= p:
            i += 1
        while j >= start and array[j] > p:
            j -= 1
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]
    array[start], array[j] = array[j], array[start]
    return j  


def QuickSort(array,start,end):
    if start < end:
        pivot=Partition(array,start,end)
        QuickSort(array,start,pivot-1)
        QuickSort(array,pivot+1,end)
    return array
# calculate inittial time:
start_time = time.time()
random_Array=[random.randint(0,10000) for x in range (0,30)]
end_time = time.time()
print("time taken to generate random array: ", end_time - start_time)
print(QuickSort(random_Array,0,len(random_Array)-1))