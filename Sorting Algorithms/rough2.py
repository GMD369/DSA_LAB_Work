import time 
import pandas
from funcs import RandomArray

def SelectionSort(array):
    for i in range(0,len(array)):
        min_index=i
        for j in range(i+1,len(array)): 
            if array[j]<array[min_index]:
                min_index=j
        if min_index!=i:
            array[i],array[min_index]=array[min_index],array[i]
    return array
  
size=5
random_array = RandomArray(size)
startTime=time.time()
print(SelectionSort(random_array))
endTime=time.time()
total=endTime-startTime
print("Time taken by Selection Sort is: ",total,"seconds")
df=pandas.DataFrame(random_array)
df.to_csv('SortedSelectionSort.csv',index=False)