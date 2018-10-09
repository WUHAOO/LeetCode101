
def Node2Num(l):
    time = 0
    val = 0
    while l:  # 当前结点不为空时
        x = l.val
        val_x = x*(10**time)
        time += 1
        val += val_x
        l = l.next
    return val

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l1 和 l2 都是一个链表，链表与list不同，没有len之类的方法，只有val，next
        # 需要的返回值也是一个链表上的结点
        # 链表的终止位置ListNode.next = None
        # 英文版的介绍了python中不存在的这个ListNode的定义，中文版没有
        num1 = Node2Num(l1)
        num2 = Node2Num(l2)
        s = num1+num2
        dummy = p = ListNode(None)  # 新建一个空表头,为循环做准备,注意需要保存表头的位置
        res = [int(i) for i in str(s)]
        res.reverse()
        for x in res:
            node = ListNode(x)
            p.next = node
            p = node
        return dummy.next

        # 还有一种办法就是计算好进位，没什么特别的难度。



