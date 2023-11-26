"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var maxheap_1 = require("./maxheap");
var data_1 = require("./data");
var heap = new maxheap_1.MaxHeap(data_1.datas);
for (var i = Math.floor(data_1.datas.length / 2); i >= 1; i--) {
    heap.maxHeapify(i);
}
console.log("heap.a", heap.a.slice(1));
