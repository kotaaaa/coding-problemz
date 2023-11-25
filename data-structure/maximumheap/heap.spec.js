"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var heap_1 = require("./heap");
var data_1 = require("./data");
console.log("datas.length / 2", Math.floor(data_1.datas.length / 2));
var heap = new heap_1.Heap(data_1.datas);
for (var i = Math.floor(data_1.datas.length / 2); i >= 1; i--) {
    heap.maxHeapify(i);
}
console.log("heap.a", heap.a);
// for (let i = 1; i < heap.a.length; i++) {
//   console.log(heap.a[i]);
// }
