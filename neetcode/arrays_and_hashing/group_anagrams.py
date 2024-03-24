from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashmap = {}

    for str in strs:
        str_list = list(str)
        str_list.sort()
        key = ''.join(str_list)

        if key in hashmap:
            hashmap.get(key).append(str)
        else:
            hashmap[key] = [str]


    print(hashmap)
    return hashmap.values()

print(groupAnagrams(['eat','tea','tan','ate','nat','bat'])) #[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(groupAnagrams(['a'])) #[['a']]