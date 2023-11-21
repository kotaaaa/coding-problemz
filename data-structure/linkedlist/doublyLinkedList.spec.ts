import { DoublyLinkedList } from "./doublyLinkedList";
import { datas } from "./data";

const list = new DoublyLinkedList();

for (let i = 0; i < datas.length; i++) {
  if (datas[i].action === "insert") {
    list.insert(datas[i].val);
  } else {
    list.deleteKey(datas[i].val);
  }
}

list.printList();
