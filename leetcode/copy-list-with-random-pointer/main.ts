/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     next: Node | null
 *     random: Node | null
 *     constructor(val?: number, next?: Node, random?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *         this.random = (random===undefined ? null : random)
 *     }
 * }
 */

let map = new Map<Node, Node>();

function copyRandomList(head: Node | null): Node | null {
  if (!head) {
    return null;
  }
  let node: Node = head;
  let retNode: Node = dfs(node);
  return retNode;
}

function dfs(node: Node): Node {
  let currentNode: Node = new Node(node.val, null, null);
  map.set(node, currentNode);
  if (node.next) {
    currentNode.next = dfs(node.next);
  }
  currentNode.random = map.get(node.random);
  return currentNode;
}
