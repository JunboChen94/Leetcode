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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode pre = new ListNode(0);
        ListNode head = pre;
        // System.out.print(l1 == null);
        // l1 = l1.next;
        // System.out.print(l1 == null);
        // l1 = l1.next;
        // System.out.print(l1 == null);
        // l1 = l1.next;
        // System.out.print(l1 == null);
        // l1 = l1.next;
        while (l1 != null && l2 != null) {
            ListNode res = new ListNode();
            int val1 = (l1 != null ? l1.val : 0);
            int val2 = (l2 != null ? l2.val : 0);
            if (val1 >= val2) {
                res.val = val2;
                
                l2 = (l2 == null ? l2 : l2.next);
            } else {
                res.val = val1;
                l1 = (l1 == null ? l1 : l1.next);
            }
            System.out.print(l1 == null);
            System.out.print(l2 == null);
            pre.next = res;
            pre = res;
            
        }
        if (l1 == null) {
            pre.next = l2;
        } else {
           pre.next = l1; 
        }
        return head.next;
    }
}