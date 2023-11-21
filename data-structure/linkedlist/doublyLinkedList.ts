export class Node {
  key: number;
  prev: Node | null;
  next: Node | null;
  constructor(key) {
    this.key = key;
    this.prev = null;
    this.next = null;
  }
}

export class DoublyLinkedList {
  nil: Node;
  constructor() {
    this.nil = new Node(null);
    this.nil.prev = this.nil;
    this.nil.next = this.nil;
  }

  insert(key: number) {
    let newNode: Node = new Node(key);
    newNode.next = this.nil.next; // Change the Node behind the new Node to the Node that was originally behind the guard.
    this.nil.next!.prev = newNode; // Change the front of the Node that was originally next to the guard to the new Node.
    this.nil.next = newNode; // Change to new Node behind the guard.
    newNode.prev = this.nil; // Specify nil before the new Node.
  }

  listSearch(key) {
    let cur: Node = this.nil.next!;
    while (cur !== this.nil && cur.key !== key) {
      cur = cur.next!;
    }
    return cur;
  }

  deleteNode(t) {
    if (t === this.nil) return;
    t.prev.next = t.next;
    t.next.prev = t.prev;
  }
  deleteFirst() {
    this.deleteNode(this.nil.next);
  }
  deleteLast() {
    this.deleteNode(this.nil.prev);
  }
  deleteKey(key) {
    this.deleteNode(this.listSearch(key));
  }
  printList() {
    let cur: Node = this.nil.next!;
    while (true) {
      if (cur === this.nil) break;
      console.log("cursor key: ", cur.key);
      cur = cur.next!;
    }
  }
}
