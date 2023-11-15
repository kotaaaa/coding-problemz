function lengthOfLongestSubstring(s: string): number {
  if (!s.length) return 0;
  let charSet: Set<string> = new Set();
  let left: number = 0;
  let right: number = 1;
  charSet.add(s[left]);
  let ans: number = 1;
  while (right < s.length) {
    if (charSet.has(s[right])) {
      charSet.delete(s[left]);
      left += 1;
    } else {
      charSet.add(s[right]);
      right += 1;
    }
    ans = Math.max(ans, charSet.size);
  }
  return ans;
}
