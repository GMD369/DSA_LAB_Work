import time
from funcs import ShuffleArray
from funcs import InsertionSort
from funcs import MergeSort
from funcs import Read_values

arr=Read_values("words.txt")

# Before shuffling runtimes count both algorithms
startTime1=time.time()
InsertionSort(arr,0,3000-1)
endTime1=time.time()
print("Insertion Sort Time before shuffling: ",endTime1-startTime1)
startTime2=time.time()
MergeSort(arr,0,3000-1)
endTime2=time.time()
print("Merge Sort Time before shuffling: ",endTime2-startTime2)

# Shuffle the random array
ShuffleArray(arr,0,3000-1)

startTime3=time.time()
InsertionSort(arr,0,3000-1)
endTime3=time.time()
print("Insertion Sort Time after shuffling: ",endTime3-startTime3)
startTime4=time.time()
MergeSort(arr,0,3000-1)
endTime4=time.time()
print("Merge Sort Time after shuffling: ",endTime4-startTime4)


# Insertion sort works faster when the array is mostly sorted beacause it does not need to make many changes but when the array is shuffled, is slows down a bit since it has to do more work to sort the data.

# Merge sort does not really care if the array is sorted or shuffled.It splits the array into smaller parts and sort them, so its speed stays almost the same whether the data is in order or not.