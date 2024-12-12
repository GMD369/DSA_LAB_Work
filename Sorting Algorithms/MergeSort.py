import time 
import pandas
from funcs import RandomArray

def Merge(array,p,q,r):
    leftHalf=array[p:q+1]
    rightHalf=array[q+1:r+1]
    i=0
    j=0
    k=p
    while i<len(leftHalf) and j<len(rightHalf):
        if leftHalf[i]<=rightHalf[j]:
            array[k]=leftHalf[i]
            i+=1
        else:
            array[k]=rightHalf[j]   
            j+=1
        k+=1
    while i<len(leftHalf):
            array[k]=leftHalf[i]
            i+=1
            k+=1
    while j<len(rightHalf):
            array[k]=rightHalf[j]
            j+=1
            k+=1
        
def MergeSort(array,start,end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
    return array


if_name_="main"

size=300
random_array = RandomArray(size)
startTime=time.time()
print(MergeSort(random_array,0,size-1))
endTime=time.time()
total=endTime-startTime
print("Time taken by Merge Sort is: ",total,"seconds")
df=pandas.DataFrame(random_array)
df.to_csv('SortedMergeSort.csv',index=False)