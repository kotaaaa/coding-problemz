import { Heap } from "./heap";
import { datas } from "./data";

let heap: Heap = new Heap(datas);
for (let i = Math.floor(datas.length / 2); i >= 1; i--) {
  heap.maxHeapify(i);
}
console.log("heap.a", heap.a.slice(1));
