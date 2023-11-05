/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     neighbors: Node[]
 *     constructor(val?: number, neighbors?: Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 */

const visited = new Map<Node, Node>();

function cloneGraph(node: Node | null): Node | null {
  if (!node) {
    return null;
  }
  return dfs(node);
}

function dfs(node: Node): Node {
  if (visited.has(node)) {
    return visited.get(node)!;
  }
  let currentNode = new Node(node.val);
  visited.set(node, currentNode);
  if (!node.neighbors.length) {
    return currentNode;
  }
  for (let n of node.neighbors) {
    currentNode.neighbors.push(dfs(n));
  }
  return currentNode;
}
