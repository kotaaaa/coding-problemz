# Overview

A priority queue is a data structure that holds a set S of data where each element has a key.
Create a program that performs insert(S, k) and extractMax(S) on a prioritized queue S that removes and returns its value. Here, the elements of the queue are integers and are considered as keys themselves.

### Constraints

```
1 ≦ k ≦ 2000000
```

### Test

```
$ tsc priorityQueue.spec.ts --lib es6,dom
$ node priorityQueue.spec.js
```

### Time complexity

- Insert: O(log(n))
- Delete: O(log(n))
