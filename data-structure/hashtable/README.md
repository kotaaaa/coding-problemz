# Overview

Implement a simple "dictionary" that executes the following commands:

- insert :Add the string "str" to the dictionary.
- find Output `yes` if the dictionary contains 5 at that point, ` no` if not.

Input The first line is given the number n of instructions. The n instructions are given in order on the following n lines. The format of the instructions is as above. Output For each find instruction, output yes or no on a single line.

### Constraints

```
The given string consists of four types of characters: `A`,`C`,`G`,`T`
1 ≦ Length of string ≦ 12
n ≦ 1000000
```

### Solution

- Hashtable
- open addressing hash table with double hashing, which is collision resolution technique.

### Test

```
$ tsc hashing.spec.ts --lib es6,dom
$ node hashing.spec.js
```

### Time complexity

- O(1) (assuming that conflict of key is neglected.)
