"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.DoublyLinkedList = exports.Node = void 0;
var Node = /** @class */ (function () {
    function Node(key) {
        this.key = key;
        this.prev = null;
        this.next = null;
    }
    return Node;
}());
exports.Node = Node;
var DoublyLinkedList = /** @class */ (function () {
    function DoublyLinkedList() {
        this.nil = new Node(null);
        this.nil.prev = this.nil;
        this.nil.next = this.nil;
    }
    DoublyLinkedList.prototype.insert = function (key) {
        var newNode = new Node(key);
        newNode.next = this.nil.next; // Change the Node behind the new Node to the Node that was originally behind the guard.
        this.nil.next.prev = newNode; // Change the front of the Node that was originally next to the guard to the new Node.
        this.nil.next = newNode; // Change to new Node behind the guard.
        newNode.prev = this.nil; // Specify nil before the new Node.
    };
    DoublyLinkedList.prototype.listSearch = function (key) {
        var cur = this.nil.next;
        while (cur !== this.nil && cur.key !== key) {
            cur = cur.next;
        }
        return cur;
    };
    DoublyLinkedList.prototype.deleteNode = function (t) {
        if (t === this.nil)
            return;
        t.prev.next = t.next;
        t.next.prev = t.prev;
    };
    DoublyLinkedList.prototype.deleteFirst = function () {
        this.deleteNode(this.nil.next);
    };
    DoublyLinkedList.prototype.deleteLast = function () {
        this.deleteNode(this.nil.prev);
    };
    DoublyLinkedList.prototype.deleteKey = function (key) {
        this.deleteNode(this.listSearch(key));
    };
    DoublyLinkedList.prototype.printList = function () {
        var cur = this.nil.next;
        while (true) {
            if (cur === this.nil)
                break;
            console.log("cursor key: ", cur.key);
            cur = cur.next;
        }
    };
    return DoublyLinkedList;
}());
exports.DoublyLinkedList = DoublyLinkedList;
