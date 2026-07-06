class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        res = []
        for val in nums:
            hash[val] = hash.get(val, 0) + 1

        for val in hash:
            res.append(val)

        for i in range(len(res) - 1):
            for j in range(len(res) - i - 1):
                if hash[res[j]] < hash[res[j + 1]]:
                    res[j], res[j + 1] = res[j + 1], res[j]
        res = res[0:k]
        return res
