class Solution:
    def addTwoNumbers(self, l1, l2):

        a = 0
        b = 0
        place = 1

        # Convert l1 linked list → number
        while l1:
            a += l1.val * place
            place *= 10
            l1 = l1.next

        place = 1

        # Convert l2 linked list → number
        while l2:
            b += l2.val * place
            place *= 10
            l2 = l2.next

        c = a + b

        # Create the answer linked list
        dummy = ListNode()
        current = dummy

        if c == 0:
            return dummy

        while c > 0:
            digit = c % 10
            current.next = ListNode(digit)
            current = current.next
            c //= 10

        return dummy.next
