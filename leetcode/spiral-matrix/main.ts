function spiralOrder(matrix) {
  if (!matrix.length || !matrix[0].length) return [];

  const rows = matrix.length;
  const cols = matrix[0].length;
  const totalElements = rows * cols;
  const visited = Array.from({ length: rows }, () => Array(cols).fill(false));

  const directions = {
    right: [0, 1],
    down: [1, 0],
    left: [0, -1],
    up: [-1, 0],
  };
  const nextDirection = {
    right: "down",
    down: "left",
    left: "up",
    up: "right",
  };

  let dir = "right";
  let r = 0,
    c = 0;
  const result = [];

  for (let i = 0; i < totalElements; i++) {
    result.push(matrix[r][c]);
    visited[r][c] = true;

    let nr = r + directions[dir][0];
    let nc = c + directions[dir][1];

    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc]) {
      r = nr;
      c = nc;
    } else {
      dir = nextDirection[dir];
      r += directions[dir][0];
      c += directions[dir][1];
    }
  }

  return result;
}
