from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for ind, num in enumerate(nums):
        remainder = target - num
        if(remainder in hashmap):
            return [hashmap[remainder], ind]
        else:
            hashmap[num] = ind

print(twoSum([2,7,11,15], 9)) #[0,1]
print(twoSum([3,2,4], 6)) #[1,2]
