/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 Do not return anything, modify head in-place instead.
 */
let nodeList: ListNode[] = [];
let nodeCount: number = 0;
function reorderList(head: ListNode | null): void {
  nodeCount = 0;
  nodeList = [];
  dfs(head);
  insertNode(head);
}

function dfs(node: ListNode) {
  nodeCount += 1;
  if (!node.next) {
    return;
  }
  dfs(node.next);
  if (nodeList.length < Math.floor(nodeCount / 2)) {
    nodeList.push(node.next);
    node.next = null;
  }
}

function insertNode(node: ListNode) {
  if (!nodeList.length) return;
  let temp = nodeList.shift();
  temp.next = node.next;
  node.next = temp;
  if (temp.next) insertNode(temp.next);
}
