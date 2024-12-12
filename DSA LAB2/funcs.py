import random

# Generate Random Array:
def RandomArray(size):
    arr=[]
    for i in range(size):
        arr.append(random.randint(-1000,10000))
    return arr

# Insertion Sort:
def InsertionSort(array,start,end):
    for i in range(start+1,end+1):
        key = array[i]
        j = i-1
        while j>=start and key<array[j]:
            array[j+1] = array[j]
            j -= 1
            array[j+1] = key
    return array

# Merge:
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
        
# MERGE SORT: 
def MergeSort(array,start,end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)

# HYBRID MERGE SORT:
def HybridMergeSort(array,start,end):
     n=32
     if (end-start+1)<=n:
          return InsertionSort(array,start,end)
     else:
        mid=(start+end)//2
        HybridMergeSort(array,start,mid)
        HybridMergeSort(array,mid+1,end)
        Merge(array,start,mid,end)

# Shuffle the Array
def ShuffleArray(array,start,end):
    if start<0 or end>len(array):
        print("Invalid start or end index")
    subarray=array[start:end+1]
    random.shuffle(subarray)
    array[start:end+1]=subarray

# BUBBLE SORT:
def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(start,end-i+start):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array


# SELECTION SORT:
def SelectionSort(array,start,end):
    for i in range(start,end):
        min_index=i
        for j in range(i+1,end):
            if array[j]<array[min_index]:
                min_index=j
        if min_index!=i:
            array[i],array[min_index]=array[min_index],array[i]
    return array

# Read Values from functions
def Read_values(filename):
    n_values=[]
    with open(filename, 'r') as file:
        for line in file:
            n_values.append(int(line.strip()))
    return n_values