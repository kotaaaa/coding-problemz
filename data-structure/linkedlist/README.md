# Overview

Implement a doubly linkedlist that accepts the following commands

- insert x: add the element with key x to the **top** of the concatenated list.
- delete x: delete the first element with key x from the linked list
- deleteFirst: delete the first element in the linked list
- deleteLast: deletes the last element in the linked list

### Test

```
$ tsc doublyLinkedList.spec.ts
$ node doublyLinkedList.spec.js
```

### Time complexity

- insert x: O(1) (In this case, node is inserted at top of the concatenated list.)
- delete x: O(n)
- delete first: O(1)
- delete last: O(1)
