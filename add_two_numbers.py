"""
You are given two non-empty linked lists 
representing two non-negative integers. 
The digits are stored in reverse order, 
and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers 
do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional 
# None이 허용되는 함수의 매개 변수에 대한 타입을 명시
# Optional[int]는 Union[int, None]과 동일

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{0}, {1}".format(self.val, self.next)

class Solution: #함수 시그니처는 단순히 쓰는 거고 강제력은 없는 듯 다른 타입을 넣어줘도 실행됨
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1.val
        b = l2.val
        upper_add = 1 if a+b>=10 else 0
        return ListNode((a+b)%10, self.getNext(l1.next, l2.next, upper_add))
    
    def getNext(self, l1, l2, upper_add):
        a = 0 if l1 == None else l1.val
        b = 0 if l2 == None else l2.val
        next_upper_add = 1 if a+b+upper_add>=10 else 0
        if l1==None and l2==None and upper_add==0 and next_upper_add==0: 
            return None
        else:
            return ListNode((a+b+upper_add)%10, self.getNext(l1.next if l1!=None else None, l2.next if l2!=None else None, next_upper_add))


if __name__ == "__main__":
    solution = Solution()
    # a = ListNode(2, ListNode(4, ListNode(3, None)))
    # b = ListNode(5, ListNode(6, ListNode(4, None)))
    # print(solution.addTwoNumbers(a, b))
    a = ListNode(1, ListNode(0, ListNode(9, None)))
    b = ListNode(5, ListNode(7, ListNode(8, None)))
    print(solution.addTwoNumbers(a, b))