export class MaxHeap {
  a: number[];
  constructor(array: number[]) {
    this.a = [0, ...array];
  }
  maxHeapify(i: number) {
    let l = 2 * i;
    let r = 2 * i + 1;
    let largest = i;
    if (l <= this.a.length && this.a[l] > this.a[i]) largest = l;
    if (r <= this.a.length && this.a[r] > this.a[largest]) largest = r;
    if (largest !== i) {
      this.swap(i, largest);
      this.maxHeapify(largest);
    }
  }
  swap(x: number, y: number) {
    let temp: number = this.a[x];
    this.a[x] = this.a[y];
    this.a[y] = temp;
  }
}
