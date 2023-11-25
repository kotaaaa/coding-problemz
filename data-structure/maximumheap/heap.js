"use strict";
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Heap = void 0;
var Heap = /** @class */ (function () {
    function Heap(array) {
        // this.a = Array.from({ length: array.length });
        this.a = __spreadArray([0], array, true);
    }
    Heap.prototype.maxHeapify = function (i) {
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
    Heap.prototype.swap = function (x, y) {
        var temp = this.a[x];
        this.a[x] = this.a[y];
        this.a[y] = temp;
    };
    return Heap;
}());
exports.Heap = Heap;
