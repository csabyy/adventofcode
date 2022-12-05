from heapq import heappop, heappush, heapify

heap = []
heapify(heap)

currentCounter = 0
for data in open("input.txt", "r"):
    if not data.strip():
        heappush(heap, -1 * currentCounter)
        currentCounter = 0
    else:
        currentCounter += int(data)
heappush(heap, -1 * currentCounter)

topN = 2
first = -1 * heappop(heap)
total = first
while topN > 0:
    total += (-1 * heappop(heap))
    topN -= 1

print(first)
print(total)
