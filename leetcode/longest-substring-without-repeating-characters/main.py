class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        ans = i = j = 0
        while i < n and j < n:
            if not s[j] in char_set:
                char_set.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                char_set.remove(s[i])
                i += 1
        return ans
