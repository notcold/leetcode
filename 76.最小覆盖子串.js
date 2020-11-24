/*
 * @lc app=leetcode.cn id=76 lang=javascript
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  if (s.length < t.length) {
    return "";
  }
  if (s === t) {
    return t;
  }
  let str = "";
  let i = 0;
  let j = 0;
  let res = t.split("");
  while (j <= s.length) {
    let mm = s.slice(i, j);
    if (check(mm, t)) {
      if (!str) {
        str = mm;
      } else {
        if (str.length > mm.length) {
          str = mm;
        }
      }
      i++;
    } else {
      j++;
    }
  }
  return str;
};

function check(source, target) {
  const arr = target.split('')
  for (let index = 0; index < source.length; index++) {
    const p = source[index];
    if (arr.includes(p)) {
      arr[arr.indexOf(p)] = "";
    }
  }
  return arr.join('').trim() ? false : true;
}
// @lc code=end
