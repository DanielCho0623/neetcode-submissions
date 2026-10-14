class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num in nums:
            freq[num] = freq.get(num,0)+1
        for num, count in freq.items():
            bucket[count].append(num)
        result = []
        while bucket and len(result) < k:
            current = bucket.pop()
            result.extend(current)
        return result