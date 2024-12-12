import time 
import pandas
from funcs import RandomArray

def SelectionSort(array,start,end):
    for i in range(start,end):
        min_index=i
        for j in range(i+1,end):
            if array[j]<array[min_index]:
                min_index=j
        if min_index!=i:
            array[i],array[min_index]=array[min_index],array[i]
    return array
  
size=30000
random_array = RandomArray(size)
startTime=time.time()
SelectionSort(random_array,0,size-1)
endTime=time.time()
total=endTime-startTime
print("Time taken by Selection Sort is: ",total,"seconds")
df=pandas.DataFrame(random_array)
df.to_csv('SortedSelectionSort.csv',index=False)