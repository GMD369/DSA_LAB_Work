import time 
import pandas
from funcs import RandomArray
from funcs import InsertionSort

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
        
def HybridMergeSort(array,start,end):
     n=4
     if (end-start+1)<=n:
          return InsertionSort(array,start,end)
     else:
        mid=(start+end)//2
        HybridMergeSort(array,start,mid)
        HybridMergeSort(array,mid+1,end)
        Merge(array,start,mid,end)
     


if_name_="main"

size=30000
random_array = RandomArray(size)
startTime=time.time()
HybridMergeSort(random_array,0,size-1)
endTime=time.time()
total=endTime-startTime
print("Time taken by HybridMerge Sort is: ",total,"seconds")
df=pandas.DataFrame(random_array)
df.to_csv('SortedHybridSort.csv',index=False)