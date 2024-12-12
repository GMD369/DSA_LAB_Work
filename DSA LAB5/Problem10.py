import time
integers=[]

def Append_Integers():
    integers
    for i in range(1,101):
        start_time=time.time()
        integers.append(i)
        end_time=time.time()
        print(f"Appending {i}: Time taken = {end_time-start_time:.10f} seconds")
  
Append_Integers()