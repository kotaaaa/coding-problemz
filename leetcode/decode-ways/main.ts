function numDecodings(s: string): number {
  let N = s.length;
  let dp = Array(N + 1).fill(0);
  dp[N] = 1;
  for (let i = N - 1; i >= 0; i--) {
    if (s[i] === "0") {
      dp[i] = 0;
      continue;
    }
    dp[i] += dp[i + 1];
    if (i + 2 <= N) {
      if (s[i] === "1" || (s[i] === "2" && Number(s[i + 1]) <= 6)) {
        dp[i] += dp[i + 2];
      }
    }
  }
  return dp[0];
}
