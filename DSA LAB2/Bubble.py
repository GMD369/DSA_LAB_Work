import time 
import pandas
from funcs import RandomArray

def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(start,end-i+start):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

size=30000
random_array = RandomArray(size)
startTime=time.time()
BubbleSort(random_array,0,size-1)
endTime=time.time()
total=endTime-startTime
print("Time taken by Bubble Sort is: ",total,"seconds")
df=pandas.DataFrame(random_array)
df.to_csv('SortedBubbleSort.csv',index=False)