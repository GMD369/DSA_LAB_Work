def remove_Integers(nums):
    return [num for num in nums if num>=0]

def find_Max_Min(nums):
    if nums:
       return max(nums), min(nums)
    else:
        return None, None

def compute_Average(nums):
    if nums:
        return sum(nums) / len(nums)
    else:
        return None

numbers = [10, -3, 25, -6, 47, 0, -2, 33]
nums=remove_Integers(numbers)
print(nums) 
max_val,min_val=find_Max_Min(nums)
if max_val is not None and min_val is not None:
    print(f"Max value is {max_val} and Min value is {min_val}")
else:
    print("The list is empty, no max or min value.")

avg=compute_Average(nums)
print(f"Average is : {avg}")


    


