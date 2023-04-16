# 우선순위 큐
# 최댓값을 빠르게 뽑아내는 자료구조
import sys, heapq

n = int(sys.stdin.readline())
heap = []
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

class Maxheap:
    def __init__(self):
        self.heap = []
    def push(self, heap, value):
        heapq.heappush(heap, -value)
        self.heap = heap
    def pop(self, heap):
        self.heap = heap
        return -heapq.heappop(self.heap)

obj = Maxheap()
for a in arr:
    if a == 0:
        if not heap:
            print(0)
        else:
            print(obj.pop(heap))
    else:
        obj.push(heap, a)

# class MaxHeap:
#     def __init__(self):
#         self.heap = []
#     def insert(self, value):
#         self.heap.append(value)
#         i = len(self.heap) - 1
#         while i>0:
#             parent = (i-1) // 2
#             if self.heap[i] > self.heap[parent]:
#                 self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
#                 i = parent
#             else:
#                 break
