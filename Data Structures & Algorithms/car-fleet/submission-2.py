class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(speed)
        arr = []
        for i in range(n):
            arr.append([position[i],(target - position[i]) / speed[i]])

        arr = sorted(arr, reverse=True)
        count = 0
        prevTime = 0
        for num in arr:
            if num[1] > prevTime:
                count += 1
                prevTime = num[1]
        return count
