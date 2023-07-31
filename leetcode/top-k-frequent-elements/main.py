class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        sorted_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(sorted_dict[i][0])
        return ans
