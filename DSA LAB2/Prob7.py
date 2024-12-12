import time 
import pandas
from funcs import InsertionSort
from funcs import MergeSort
from funcs import RandomArray
from funcs import HybridMergeSort
from funcs import BubbleSort
from funcs import SelectionSort
from funcs import Read_values

n_values=Read_values("Nvalues.txt")
result=[]
for n in n_values:
    size=n
    random_array = RandomArray(size)

    startTime=time.time()
    InsertionSort(random_array,0,size-1)
    endTime=time.time()
    insertion=endTime-startTime

    startTime1=time.time()
    MergeSort(random_array,0,size-1)
    endTime1=time.time()
    merge=endTime1-startTime1

    startTime2=time.time()
    HybridMergeSort(random_array,0,size-1)
    endTime2=time.time()
    hybrid=endTime2-startTime2

    startTime3=time.time()
    SelectionSort(random_array,0,size-1)
    endTime3=time.time()
    selection=endTime3-startTime3

    startTime4=time.time()
    BubbleSort(random_array,0,size-1)
    endTime4=time.time()
    bubble=endTime4-startTime4
    
   
    result.append({
        'Values of n':n,
        'Insertion Sort':insertion,
        'MergeSort':merge,
        'HybridMergeSort':hybrid,
        'SelectionSort':selection,
        'BubbleSort':bubble
    })
    print(n,insertion,merge,hybrid,selection,bubble)
df=pandas.DataFrame(result)
df.to_csv('Runtime.csv',index=False)
print("Runtime Results are saved in Runtime.CSV")  