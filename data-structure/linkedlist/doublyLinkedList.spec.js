"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var doublyLinkedList_1 = require("./doublyLinkedList");
var data_1 = require("./data");
var list = new doublyLinkedList_1.DoublyLinkedList();
for (var i = 0; i < data_1.datas.length; i++) {
    if (data_1.datas[i].action === "insert") {
        list.insert(data_1.datas[i].val);
    }
    else {
        list.deleteKey(data_1.datas[i].val);
    }
}
list.printList();
