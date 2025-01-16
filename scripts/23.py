# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        begin = None
        ans = None
        h = []
        for i in range(k):
            if lists[i] is not None:
                heappush(h, (lists[i].val, i))
        while(len(h)):
            smallest, ind = heappop(h)            
            if ans is None:
                ans = ListNode(smallest)
                begin = ans
            else:
                ans.next = ListNode(smallest)
                ans = ans.next
            if lists[ind].next is not None:
                lists[ind] = lists[ind].next
                heappush(h, (lists[ind].val, ind))
        return begin