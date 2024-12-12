# DSA LAB WEEK 1  PROBLEMS


# PROBLEM 1:

def SearchA(Arr,X):
    indices=[]
    for i in range(len(Arr)):
        if Arr[i]==X:
            indices.append(i)
    return indices

numbers=[22,2,1,7,11,13,5,2,9] 
 
 
x=int(input("Enter the number: "))
indices=SearchA(numbers,x)

if indices:
    print("Index: ",end="")
    for i in range(len(indices)):
        if i== len(indices)-1:
            print(indices[i])
        else:
            print(indices[i], end=",")
else:
    print("element not found!")


# PROBLEM 2:

def SearchB(Arr,X):
    low=0
    high=len(Arr)-1
    indices=[]
    while low<=high:
        mid=(low+high)//2
        if Arr[mid]==X:
            indices.append(mid)
            i=mid-1
            while i>=0 and Arr[i]==X:
                indices.append(i)
                i-=1
            j=mid+1
            while j<len(Arr) and Arr[j]==X:
                indices.append(j)
                j+=1
            break
        elif Arr[mid]<X:
            low=mid+1
        else:
            high=mid-1
    return sorted(indices)

X=[22,2,1,7,11,13,5,2,9] 
x=int(input("Enter the number: "))
indices2=SearchB(sorted(X),x)

if indices2:
    print("Index: ",end="")
    for i in range(len(indices2)):
        if i== len(indices2)-1:
            print(indices2[i])
        else:
            print(indices2[i], end=",")
else:
    print("element not found!")


# PROBLEM 3:

def Minimum(Arr,starting,ending):
    start_index=starting
    for i in range(starting,ending+1):
        if Arr[i]<Arr[start_index]:
            start_index=i
    return start_index

arr = [3, 4, 7, 8, 0, 1, 23, -2, -5]
starting=4
ending=7
min_index=Minimum(arr,starting,ending)
print(min_index)


# PROBLEM 4:

def Minimum(Arr,starting,ending):
    start_index=starting
    for i in range(starting,ending+1):
        if Arr[i]<Arr[start_index]:
            start_index=i
    return start_index

def Sort4(Arr):
    n=len(Arr)
    for i in range(n):
        min_index=Minimum(Arr,i,n-1)
        if min_index!=i:
             Arr[i],Arr[min_index]=Arr[min_index],Arr[i]
    return Arr

Arr=[4,8,2,-4,-6,5,7,-3,-1]
sort_Arr=Sort4(Arr)
print(sort_Arr)


# PROBLEM 5:

def StringReverse(s,starting ,ending):
    sub_str=s[starting:ending+1]
    return sub_str[::-1]

s = "University of Engineering and Technology Lahore"
starting=27
ending=39
print(StringReverse(s,starting,ending))


# PROBLEM 6:

def SumInterative(number):
    total=0
    while number>0:
        remainder=number%10
        total+=remainder
        number=number//10
    return total

def SumRecursive(number):
    if number==0:
        return 0
    else:
        return number%10+ SumRecursive(number//10)
    
number=1524
print("Iterative Sum: ",SumInterative(number))
print("Recursive Sum: ",SumRecursive(number))


# PROBLEM 7:


def ColumnWiseSum(Mat):
    num_rows=len(Mat)
    num_cols=len(Mat[0])
    print("ColumnWise: ",end="")

    for i in range(num_cols):
        col_sums=0
        for j in range(num_rows):
            col_sums+=Mat[j][i]
        print(col_sums, end=" ")
    return col_sums

def RowWiseSum(Mat):
    print("RowWise:")
    for row in Mat:
        row_sums=sum(row)
        print(row_sums)

A = [
    [1, 13, 13],
    [5, 11, 6],
    [4, 4, 9]
]
ColumnWiseSum(A)
RowWiseSum(A)


# PROBLEM 8:


def SortedMerge(Arr1,Arr2):
    result=[]
    i=0
    j=0
    while i<len(Arr1) and j<len(Arr2):
        if Arr1[i]<Arr2[j]:
            result.append(Arr1[i])
            i+=1
        else :
            result.append(Arr2[j])
            j+=1
    while i<len(Arr1):
        result.append(Arr1[i])
        i+=1
    while j<len(Arr2):
        result.append(Arr2[j])
        j+=1
    return result

A = [0,3,4,10,11] 
B = [1,8,13,24] 
merged_arr=SortedMerge(A,B)
print(merged_arr)


# PROBLEM 9:


def PalindromRecursive(str):
    if len(str) == 0 or len(str) == 1:
        return "palindrome"
    if str[0] == str[-1]:
        return PalindromRecursive(str[1:-1])
    else:
        return False

print(PalindromRecursive("radar"))


# PROBLEM 10:

def Sort10(Arr):
    negatives=[num for num in Arr if num<0]
    positives=[num for num in Arr if num>=0]
    return sorted(negatives)+sorted(positives)


a=[10, -1, 9, 20, -3, -8, 22, 9, 7] 
print(Sort10(a))


