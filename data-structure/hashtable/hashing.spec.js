"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var hashing_1 = require("./hashing");
var data_1 = require("./data");
var hashing = new hashing_1.Hashing();
for (var i = 0; i < data_1.datas.length; i++) {
    if (data_1.datas[i].action === "insert") {
        hashing.insert(data_1.datas[i].val);
    }
    else {
        if (hashing.find(data_1.datas[i].val) >= 0) {
            console.log("yes");
        }
        else {
            console.log("no");
        }
    }
}
