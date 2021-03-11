/*
 * @lc app=leetcode.cn id=148 lang=javascript
 *
 * [148] 排序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    const target = head
    // 归并排序
    /** 
     * merge(l1, l2)，双路归并，我相信这个操作大家已经非常熟练的，就不做介绍了。
     *   cut(l, n)，可能有些同学没有听说过，它其实就是一种 split 操作，即断链操作。不过我感觉使用 cut 更准确一些，它表示，将链表 l 切掉前 n 个节点，并返回后半部分的链表头。
     */
    const cut = (linkList,,n) => {
      
    }
    const merge = (l1,l2) => {
        
    }
    

};
// @lc code=end

