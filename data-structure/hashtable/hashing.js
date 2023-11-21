"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Hashing = void 0;
var Hashing = /** @class */ (function () {
    function Hashing() {
        this.M = 1046527;
        this.H = Array.from({ length: this.M }, function () { return ""; });
    }
    Hashing.prototype.getChar = function (ch) {
        if (ch === "A") {
            return 1;
        }
        else if (ch === "C") {
            return 2;
        }
        else if (ch === "G") {
            return 3;
        }
        else if (ch === "T") {
            return 4;
        }
        else {
            return 0;
        }
    };
    Hashing.prototype.getKey = function (str) {
        var sum = 0;
        var p = 1;
        for (var i = 0; i < str.length; i++) {
            sum += p * this.getChar(str[i]);
            p *= 5;
        }
        return sum;
    };
    Hashing.prototype.h1 = function (key) {
        return key % this.M;
    };
    Hashing.prototype.h2 = function (key) {
        return 1 + (key % (this.M - 1));
    };
    Hashing.prototype.find = function (str) {
        var key = this.getKey(str);
        for (var i = 0; i < this.M; i++) {
            var h = (this.h1(key) + i * this.h2(key)) % this.M;
            if (this.H[h] === str) {
                return h; // Key found
            }
            else if (this.H[h] === "" || this.H[h] === undefined) {
                return -1; // Empty slot found
            }
        }
        return -1;
    };
    Hashing.prototype.insert = function (str) {
        var key = this.getKey(str);
        for (var i = 0; i < this.M; i++) {
            var h = (this.h1(key) + i * this.h2(key)) % this.M;
            if (this.H[h] === str) {
                return h; // Key found
            }
            else if (this.H[h] === "" || this.H[h] === undefined) {
                this.H[h] = str;
                return 0;
            }
        }
        return -1;
    };
    return Hashing;
}());
exports.Hashing = Hashing;
