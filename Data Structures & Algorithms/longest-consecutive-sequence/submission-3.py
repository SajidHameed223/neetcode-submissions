class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap=set(nums)
        counter = 0 
        print(hashmap)
        output = 1
        for num in hashmap:
            if num-1 in hashmap:
                while num-1 in hashmap:
                    output +=1 
                    num -= 1
                counter = max(counter , output)
                
                output=1
            else:
                output = 1 
            counter = max(counter , output)
        return counter 