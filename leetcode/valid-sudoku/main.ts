function isValidSudoku(board: string[][]): boolean {
  let board2: string[][] = board[0].map((_, colIndex) =>
    board.map((row) => row[colIndex])
  );
  if (!check(board)) return false;
  if (!check(board2)) return false;

  let arrSet: Set<string>[] = Array.from({ length: 9 }, () => new Set());
  let ans: boolean = true;
  board.map((row, _y) => {
    row.map((val, _x) => {
      if (arrSet[Math.floor(_y / 3) + 3 * Math.floor(_x / 3)].has(val)) {
        ans = false;
        return;
      }

      if (val !== ".") {
        arrSet[Math.floor(_y / 3) + 3 * Math.floor(_x / 3)].add(val);
      }
    });
  });
  return ans;
}

function check(map: string[][]): boolean {
  let set: Set<string> = new Set();
  let checked: boolean = true;
  map.map((row) => {
    set = new Set();
    row
      .filter((val) => val !== ".")
      .map((val) => {
        if (set.has(val)) {
          checked = false;
        }
        set.add(val);
      });
  });
  return checked;
}
