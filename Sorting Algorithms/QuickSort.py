from funcs import RandomArray


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


array=RandomArray(100000)
print(QuickSort(array,0,len(array)-1))

