def printMatrix(A,starting_index,rows,columns):
    
    for i in range(starting_index[0],starting_index[0]+rows):
        for j in range(starting_index[1],starting_index[1]+columns):
            print(A[i][j],end=" ")
        print()    


A = [
   [1, 2, 3, 4, 5],
   [6, 7, 8, 9, 10],
   [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

printMatrix(A,(2,1),2,3)      



def MatAdd(A,B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
    
    
A = [
   [1,2,3],
   [4,5,6]
]         
B = [
   [7,8,9],
   [10,11,12]
]   
print(MatAdd(A,B))
            
def MatAddPartial(A, B, start, size) :
    
    results = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            results[i][j] = A[start[0]+i][start[1]+j] + B[start[0]+i][start[1]+j]
        return results
        
#print(MatAddPartial(A,B,(1,1),1))   

def MatMul(A,B):
    rowsA = len(A)
    colsA = len(A[0])
    colsB = len(B[0])
    results = [[0 for i in range(colsA)] for j in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for p in range(colsA):
                results[i][j]+= A[i][p] * B[p][j]
    return results

C = [
   [1,2],
   [3,4]
]       
D = [
   [5,6],
   [7,8]
]    
result = MatMul(C,D)
for i in result:
   print(i)        
    
    
    
def MatMulRecursive(A,B):
    n = len(A)
    
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n//2
    A11 , A12, A21, A22 = SplitMatrices(A)
    B11, B12 , B21, B22 = SplitMatrices(B)
    C11 = MatAdd(MatMulRecursive(A11,B11),MatMulRecursive(A12,B21))
    C12 = MatAdd(MatMulRecursive(A11,B12),MatMulRecursive(A12,B22))
    C21 = MatAdd(MatMulRecursive(A21,B11),MatMulRecursive(A22,B21))
    C22 = MatAdd(MatMulRecursive(A21,B12),MatMulRecursive(A22,B22))
    
    
    return CombineMatrices(C11,C12,C21,C22)
    
def CombineMatrices(C11,C12,C21,C22):
    A = [C11[i] + C12[i] for i in range(len(C11))]
    B = [C21[i] +C22[i] for i in range(len(C21))]
    return A + B   
    
    
    
    
def SplitMatrices(A):
    mid = len(A)//2
    A11 = [row[:mid] for row in A[:mid]]  
    A12 = [row[mid:]for row in A[:mid]]
    A21 = [row[:mid]for row in A[mid:]]
    A22 = [row[mid:]for row in A[mid:]]      
    return A11,A12,A21,A22


E = [[1,2],
     [3,4]]
F = [[5,6],
     [7,8]]
ans = MatMulRecursive(E,F)
for j in ans:
   print(j)
 
def MatMulStrassen(A,B):
     n = len(A)
    
     if n == 1:
        return [[A[0][0] * B[0][0]]]
    
     mid = n//2
     A11 , A12, A21, A22 = SplitMatrices(A)
     B11, B12 , B21, B22 = SplitMatrices(B)
     M1 = MatMulStrassen(MatAdd(A11, A22), MatAdd(B11, B22))  # M1 = (A11 + A22) * (B11 + B22)
     M2 = MatMulStrassen(MatAdd(A21, A22), B11)               # M2 = (A21 + A22) * B11
     M3 = MatMulStrassen(A11, MatSub(B12, B22))               # M3 = A11 * (B12 - B22)
     M4 = MatMulStrassen(A22, MatSub(B21, B11))               # M4 = A22 * (B21 - B11)
     M5 = MatMulStrassen(MatAdd(A11, A12), B22)               # M5 = (A11 + A12) * B22
     M6 = MatMulStrassen(MatSub(A21, A11), MatAdd(B11, B12))  # M6 = (A21 - A11) * (B11 + B12)
     M7 = MatMulStrassen(MatSub(A12, A22), MatAdd(B21, B22))  # M7 = (A12 - A22) * (B21 + B22)

     C11 = MatAdd(MatSub(MatAdd(M1, M4), M5), M7)  # C11 = M1 + M4 - M5 + M7
     C12 = MatAdd(M3, M5)                          # C12 = M3 + M5
     C21 = MatAdd(M2, M4)                          # C21 = M2 + M4
     C22 = MatAdd(MatSub(MatAdd(M1, M3), M2), M6)  # C22 = M1 + M3 - M2 + M6

     return CombineMatrices(C11, C12, C21, C22)


def MatSub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
A = [[1,2],[3,4]]   
B = [[5,6],[7,8]]
ans =MatMulStrassen(A,B)
for row in ans:
    print(row)