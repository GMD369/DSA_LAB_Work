import time 
import pandas
from funcs import RandomArray

def InsertionSort(array,start,end):
    for i in range(start+1,end+1):
        key = array[i]
        j = i-1
        while j>=start and key<array[j]:
            array[j+1] = array[j]
            j -= 1
            array[j+1] = key
    return array


if_name_="main"

size=30000
random_array = RandomArray(size)
startTime=time.time()
InsertionSort(random_array,0,size-1)
endTime=time.time()
total=endTime-startTime
print("Time taken by Insertion Sort is: ",total,"seconds")
df=pandas.DataFrame(random_array)
df.to_csv('SortedInsertionSort.csv',index=False)