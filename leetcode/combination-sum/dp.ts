function combinationSum(candidates: number[], target: number): number[][] {
  const dp: number[][][] = Array.from({ length: target + 1 }, () => []);
  dp[0] = [[]];
  for (const candidate of candidates) {
    for (let i = candidate; i <= target; i++) {
      for (const prevCombi of dp[i - candidate]) {
        dp[i].push([...prevCombi, candidate]);
      }
    }
  }
  return dp[target];
}
