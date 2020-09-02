/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode pre = new ListNode(0);
        ListNode head = pre;
        
        int addon = 0;
        while(l1 != null || l2 != null || addon != 0) {
            ListNode cur = new ListNode();
            int sum = (l1 != null ? l1.val:0) + addon + (l2 != null ? l2.val:0);
            addon = sum / 10;
            sum = (sum > 9 ? sum - 10 : sum);
            cur.val = sum;
            pre.next = cur;
            pre = cur;
            l1 = (l1 == null ? l1 : l1.next);
            l2 = (l2 == null ? l2 : l2.next);
            
        }
        return head.next;
    }
}