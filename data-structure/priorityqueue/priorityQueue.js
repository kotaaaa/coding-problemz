"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.PriorityQueue = void 0;
var PriorityQueue = /** @class */ (function () {
    function PriorityQueue() {
        var _this = this;
        this.INFTY = 1 << 30;
        this.MAX = 2000000;
        this.H = 0;
        this.a = Array.from({ length: this.MAX }, function () { return -_this.INFTY; });
        this.H = 0;
    }
    PriorityQueue.prototype.extract = function () {
        if (this.H < 1)
            return null;
        var maxv = this.a[1];
        this.a[1] = this.a[this.H];
        this.a[this.H] = -this.INFTY;
        this.H -= 1;
        this.maxHeapify(1);
        return maxv;
    };
    PriorityQueue.prototype.increaseKey = function (i, key) {
        // if (key < this.a[i]) return;
        this.a[i] = key;
        while (i > 1 && this.a[Math.floor(i / 2)] < this.a[i]) {
            this.swap(Math.floor(i / 2), i);
            i = Math.floor(i / 2);
        }
    };
    PriorityQueue.prototype.insert = function (key) {
        this.H += 1;
        // this.a[this.H] = -this.INFTY;
        this.increaseKey(this.H, key);
    };
    PriorityQueue.prototype.maxHeapify = function (i) {
        var l = 2 * i;
        var r = 2 * i + 1;
        var largest = i;
        if (l <= this.a.length && this.a[l] > this.a[i])
            largest = l;
        if (r <= this.a.length && this.a[r] > this.a[largest])
            largest = r;
        if (largest !== i) {
            this.swap(i, largest);
            this.maxHeapify(largest);
        }
    };
    PriorityQueue.prototype.swap = function (x, y) {
        var temp = this.a[x];
        this.a[x] = this.a[y];
        this.a[y] = temp;
    };
    return PriorityQueue;
}());
exports.PriorityQueue = PriorityQueue;
