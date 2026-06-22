class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        arr = []
        for i in range(len(strs)):
            sorted_ch = "".join(sorted(strs[i]))
            if sorted_ch not in hashmap:
                hashmap[sorted_ch] = len(arr)
                arr.append([])
            arr[hashmap[sorted_ch]].append(strs[i])
        return arr    