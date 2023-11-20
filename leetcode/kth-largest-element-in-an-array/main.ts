function findKthLargest(nums: number[], k: number): number {
  const mpq = new MaxPriorityQueue();
  for (let n of nums) {
    mpq.enqueue(n);
  }
  let ans: number = 0;
  for (let i = 0; i < k; i++) {
    ans = mpq.dequeue().element;
  }
  return ans;
}
