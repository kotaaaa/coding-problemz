/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
  let l: number = 0,
    r: number = 0;
  while (r < nums.length) {
    if (nums[r] !== 0) {
      swap(nums, l, r);
      r += 1;
      l += 1;
    } else {
      r += 1;
    }
  }
}

function swap(nums, a, b) {
  const temp = nums[a];
  nums[a] = nums[b];
  nums[b] = temp;
}
