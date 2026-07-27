import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create frequency map of nums
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Initialise min-heap
        heap = []

        # For every element in freqmap:
        for num in count.keys():
            # Append (frequency, value) into min-heap
            heapq.heappush(heap, (count[num], num))

            # If length of heap > k:
            if len(heap) > k:
                # pop the smallest value from heap
                heapq.heappop(heap)

        # Initialise result []
        result = []

        # For i in range of k:
        for i in range(k):
            # result appended with heap(frequency, value)[1]
            result.append(heapq.heappop(heap)[1])

        # Return result
        return result