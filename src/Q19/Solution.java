package Q19;

class Solution {
    public static ListNode removeNthFromEnd(ListNode head, int n) {
        int i = 0;
        ListNode current = head;
        ListNode remove = null;
        ListNode before = null;
        while (current != null) {
            if (i < n) {
                remove = head;
            } else if (remove != null){
                before = remove;
                remove = remove.next;
            }
            current = current.next;
            i++;
        }
        if (i == n) {
            return head.next;
        }
        before.next = remove.next;
        return head;
    }

    public static void main(String[] args) {
        ListNode fifth = new ListNode(5);
        ListNode forth = new ListNode(4, fifth);
        ListNode third = new ListNode(3, forth);
        ListNode second = new ListNode(2, third);
        ListNode head = new ListNode(1, second);

        ListNode answer = removeNthFromEnd(head, 5);
        while (answer != null) {
            System.out.println(answer.val);
            answer = answer.next;
        }
    }
}