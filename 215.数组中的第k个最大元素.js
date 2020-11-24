/*
 * @lc app=leetcode.cn id=215 lang=javascript
 *
 * [215] 数组中的第K个最大元素
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
  const buildHeap = (arr) => {
    const n = arr.length;
    for (let index = n >> 1; index >= 0; index--) {
      heapify(arr, n, index);
    }
  };
  const heapify = (arr, n, i) => {
    while (true) {
      let maxPos = i;
      if (i * 2 + 1 < n && arr[i] < arr[i * 2 + 1]) {
        maxPos = i * 2 + 1;
      }
      if (i * 2 + 2 < n && arr[maxPos] < arr[i * 2 + 2]) {
        maxPos = i * 2 + 2;
      }
      if (i === maxPos) break;
      swap(arr, i, maxPos);
      i = maxPos;
    }
  };
  const swap = (arr, a, b) => {
    const temp = arr[b];
    arr[b] = arr[a];
    arr[a] = temp;
  };
  buildHeap(nums);
  let max;
  while (k > 0) {
    swap(nums, 0, nums.length - 1);
    max = nums.pop();
    heapify(nums, nums.length, 0);
    k--;
  }
  return max;
};
// @lc code=end
