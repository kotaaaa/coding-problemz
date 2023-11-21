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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let num: number = 0;
  dfs(head);
  function dfs(node: ListNode) {
    if (!node) {
      return;
    }
    dfs(node.next);
    if (n === num) {
      node.next = node.next.next;
    }
    num += 1;
  }
  if (num === n) {
    return head.next;
  }
  return head;
}
