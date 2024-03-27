from typing import List

def maxProduct( nums: List[int]) -> int:
    current_max = 1
    current_min = 1
    output = nums[0]
    for num in nums:
        temp_max = max(num * current_max, num, num * current_min)
        current_min = min(num * current_max, num, num * current_min)
        current_max = temp_max
        output = max(output, current_max)

    #starting with [2, 3, -2, 4]
    #loop1: temp_max = 2, current_min = 2, output = 2
    #loop2: temp_max = 6, current_min = 3, output = 6
    #loop3: temp_max = -2, current_min = -12, output = 6
    #loop4: temp_max = 4, current_min = -48, output = 6
    return output

print(maxProduct([2,3,-2,4])) # output = 6