// https://leetcode.com/problems/letter-combinations-of-a-phone-number/
function letterCombinations(digits: string): string[] {
  if (!digits.length) {
    return [];
  }
  const letters = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  };
  let ans: string[] = [];
  const buttons: string[][] = [];
  for (let i = 0; i < digits.length; i++) {
    buttons.push(letters[digits[i]]);
  }
  ans = buttons.shift()!;
  while (buttons.length) {
    let number = buttons.shift()!;
    let tmpAnswer: string[] = [];
    for (let i = 0; i < ans.length; i++) {
      for (let j = 0; j < number.length; j++) {
        tmpAnswer.push(ans[i] + String(number[j]));
      }
    }
    ans = tmpAnswer;
  }
  return ans;
}
