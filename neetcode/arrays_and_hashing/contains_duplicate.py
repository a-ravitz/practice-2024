from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    num_set = set()
    for i in nums:
        if i in num_set:
            return True 
        else:
            num_set.add(i)
    return False
    
print(containsDuplicate([1,2,3,1])) # True
print(containsDuplicate([1,2,3,4,5,6,7,8])) # False