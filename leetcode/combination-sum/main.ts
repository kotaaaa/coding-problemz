function combinationSum(candidates: number[], target: number): number[][] {
  let result: number[][] = [];
  function backtrack(remaining: number, combo: number[], start: number) {
    if (remaining === 0) {
      result.push([...combo]);
      return;
    }

    if (remaining < 0) {
      return;
    }

    for (let i = start; i < candidates.length; i++) {
      combo.push(candidates[i]);
      backtrack(remaining - candidates[i], combo, i);
      combo.pop();
    }
  }
  backtrack(target, [], 0);
  return result;
}
