/*
 * @lc app=leetcode.cn id=419 lang=javascript
 *
 * [419] 甲板上的战舰
 */

// @lc code=start
/**
 * @param {character[][]} board
 * @return {number}
 */
var countBattleships = function(board) {
  let count = 0

  const dfs = (row, col) => {
      //如果超出范围则终止，遇到'.'也终止
      if (row < 0 || row >= board.length || col < 0 || col >= board[0].length || board[row][col] == '.') {
          return
      }
      //下沉
      board[row][col] = '.'
      //向四周扩散
      dfs(row + 1, col)
      dfs(row - 1, col)
      dfs(row, col + 1)
      dfs(row, col - 1)
  }

  for (let row = 0; row < board.length; row++) {
      for (let col = 0; col < board[0].length; col++) {
          if (board[row][col] == 'X') {
              count++
              dfs(row, col)
          }
      }
  }

  return count
};
// @lc code=end

