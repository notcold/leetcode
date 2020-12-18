/*
 * @lc app=leetcode.cn id=739 lang=javascript
 *
 * [739] 每日温度
 */

// @lc code=start
/**
 * @param {number[]} T
 * @return {number[]}
 */
var dailyTemperatures = function(T) {
  let stack = []
  let res = []
  for (let index = 0; index < T.length; index++) {
    while(stack.length){
      if(T[stack[stack.length-1]]<T[index]){
        let j = stack.pop()
        res[j] = index - j 
      }else{
        break
      }
    }
    stack.push(index)
  }
  while(stack.length){
    let j = stack.pop()
    res[j] = 0
  }
  return res 
};
// @lc code=end

