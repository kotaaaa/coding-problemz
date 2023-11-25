export class PriorityQueue {
  INFTY: number = 1 << 30;
  MAX: number = 2000000;
  H: number = 0;
  a: number[];
  constructor() {
    this.a = Array.from({ length: this.MAX }, () => -this.INFTY);
    this.H = 0;
  }
  extract(): number | null {
    if (this.H < 1) return null;
    let maxv: number = this.a[1];
    this.a[1] = this.a[this.H];
    this.a[this.H] = -this.INFTY;
    this.H -= 1;
    this.maxHeapify(1);
    return maxv;
  }
  increaseKey(i: number, key: number) {
    if (key < this.a[i]) return;
    this.a[i] = key;
    while (i > 1 && this.a[Math.floor(i / 2)] < this.a[i]) {
      this.swap(Math.floor(i / 2), i);
      i = Math.floor(i / 2);
    }
  }
  insert(key: number) {
    this.H += 1;
    this.a[this.H] = -this.INFTY;
    this.increaseKey(this.H, key);
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
