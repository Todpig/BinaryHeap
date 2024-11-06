from src.binary_heap.binary_heap import BinaryHeap

wait_time = 500

def verify_empty_heap(binary_heap: BinaryHeap, step: int):
    if binary_heap.size > 0:
            high_priority_value = binary_heap.get_high_priority()
            return f"STEP {step} - Highest Priority: {high_priority_value}"
   
    return f"STEP {step} - Heap is empty"