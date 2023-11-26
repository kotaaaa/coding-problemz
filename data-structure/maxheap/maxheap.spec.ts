import { MaxHeap } from "./maxheap";
import { datas } from "./data";

let heap: MaxHeap = new MaxHeap(datas);
for (let i = Math.floor(datas.length / 2); i >= 1; i--) {
  heap.maxHeapify(i);
}
console.log("heap.a", heap.a.slice(1));
