function isValidSudoku(board: string[][]): boolean {
  for (let i = 0; i < board.length; i++) {
    const set = new Set();
    for (let j = 0; j < board.length; j++) {
      const rowVal = board[i][j];
      const colVal = board[j][i];
      const boxVal =
        board[3 * Math.floor(i / 3) + Math.floor(j / 3)][3 * (i % 3) + (j % 3)];

      const rowKey = `rowVal_${rowVal}`;
      const colKey = `colVal_${colVal}`;
      const boxKey = `boxVal_${boxVal}`;

      if (rowVal !== ".") {
        if (set.has(rowKey)) return false;
        set.add(rowKey);
      }

      if (colVal !== ".") {
        if (set.has(colKey)) return false;
        set.add(colKey);
      }

      if (boxVal !== ".") {
        if (set.has(boxKey)) return false;
        set.add(boxKey);
      }
    }
  }

  return true;
}
