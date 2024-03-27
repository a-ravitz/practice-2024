from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    answer = [1] * len(nums) #make an array of 1's length of nums

    # start at 1 and loop through nums replacing the current index in answer with the value
    # answer[i-1] * nums[i-1]

    #starting with nums [1, 2, 3, 4]
    #first loop answer[1] = answer[0] * nums[0] (1 * 1)
    #[1, 1, 1, 1]
    #second loop answer[2] = answer[1] * nums[1] (1 * 2)
    #[1, 1, 2, 1]
    #third loop answer[3] = answer[2] * nums[2] (2 * 3)
    #[1, 1, 2, 6] 
    for i in range(1, len(nums)):
        answer[i] = answer[i-1] * nums[i-1]
        print(i, answer)

    #right = 1 - [1, 1, 2, 6] - answer[3] = 6 * 1, right = 1 * 4 
    #right = 4 - [1, 1, 8, 6] - answer[2] = 2 * 4, right = 4 * 3
    #right = 12 - [1, 12, 8, 6] - answer[1] = 1 * 12, right = 12 * 2
    #right = 24 - [24, 12, 8, 6] - 

    right = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]
        
    return answer

print(productExceptSelf([1,2,3,4])) # output = [24,12,8,6]
