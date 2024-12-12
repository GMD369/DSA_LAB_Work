import time 
import pandas
from funcs import RandomArray

def InsertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


if_name_="main"

size=5
random_array = RandomArray(size)
startTime=time.time()
print(InsertionSort(random_array))
endTime=time.time()
total=endTime-startTime
print("Time taken by Insertion Sort is: ",total,"seconds")
df=pandas.DataFrame(random_array)
df.to_csv('SortedInsertionSort.csv',index=False)