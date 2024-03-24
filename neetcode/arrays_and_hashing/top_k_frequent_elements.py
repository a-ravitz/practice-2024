from typing import List


def topKFrequent( nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range (len(nums) + 1)] # makes an array of empty arrays the length of nums + 1

    #store each number and the number of occurrences 
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    #loop through count.items and append the number to the appropriate array in the freq array
        #value #key 
    for index, number in count.items():
        freq[number].append(index)

    result = []

    #loop through freq array starting from the end going to index 0
    #loop through each individual array and append the values to the result array until results' length == k
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:   
            result.append(n)

            if len(result) == k:
                return result

print(topKFrequent([1,1,1,2,2,3], 2)) #[1,2]
print(topKFrequent([1], 1)) #[1]