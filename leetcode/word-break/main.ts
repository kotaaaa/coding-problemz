function wordBreak(s: string, wordDict: string[]): boolean {
  let wordSet: Set<string> = new Set(wordDict);
  let dp: boolean[] = Array(s.length + 1).fill(false);
  dp[0] = true;
  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
      console.log(i, j, dp[j], wordSet.has(s.substring(j, i)));
      if (dp[j] && wordSet.has(s.substring(j, i))) {
        dp[i] = true;
      }
    }
  }
  return dp[s.length];
}
