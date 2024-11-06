from src.binary_heap.binary_heap import BinaryHeap

def verify_empty_heap(binary_heap: BinaryHeap):
    if binary_heap.size > 0:
            high_priority_value = binary_heap.get_high_priority()
            return f"Highest Priority: {high_priority_value}"
   
    return "Heap is empty"