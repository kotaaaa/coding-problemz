"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var priorityQueue_1 = require("./priorityQueue");
var data_1 = require("./data");
var priorityQueue = new priorityQueue_1.PriorityQueue();
for (var i = 0; i < data_1.datas.length; i++) {
    if (data_1.datas[i].action === "insert") {
        priorityQueue.insert(data_1.datas[i].val);
    }
    else {
        console.log(priorityQueue.extract());
    }
}
