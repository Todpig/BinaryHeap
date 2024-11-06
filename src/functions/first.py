import pygame
from src.utils import verify_empty_heap
from src.binary_heap.binary_heap import BinaryHeap
from src.utils import wait_time

def first_set_of_numbers(binary_heap: BinaryHeap):
    step = 1
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Binary Heap Tree Visualization")
    font = pygame.font.SysFont(None, 36)

    array_values = [10, 5, 20, 1, 15, 30, 25]

    # Step 1: Insert values into the binary heap
    for value in array_values:
        binary_heap.insert(value)
        binary_heap.display_heap(screen, font)
        priority_text = verify_empty_heap(binary_heap, step)
        priority_surface = font.render(priority_text, True, (255, 255, 255))
        screen.blit(priority_surface, (20, 20))
        pygame.display.flip()
        pygame.time.delay(wait_time)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    pygame.time.delay(wait_time)

    # Step 2: Change priorities
    values = {
        3: 50,
        1: 8  
    }
    for index in list(values.keys()):
        binary_heap.change_priority(index, values[index])
        binary_heap.display_heap(screen, font)
        
        priority_text = verify_empty_heap(binary_heap, step)
        
        priority_surface = font.render(priority_text, True, (255, 255, 255))
        screen.blit(priority_surface, (20, 20))  
        pygame.display.flip()  
        
        pygame.time.delay(wait_time)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    pygame.time.delay(wait_time)

    # Step 3: Remove three elements from the heap
    for _ in range(3):
        binary_heap.remove()
        binary_heap.display_heap(screen, font)  
        priority_text = verify_empty_heap(binary_heap, step)
        priority_surface = font.render(priority_text, True, (255, 255, 255))
        screen.blit(priority_surface, (20, 20))  
        pygame.display.flip()
        
        pygame.time.delay(wait_time)

    # Step 4: Heapsort
    for _ in range(binary_heap.size):
        binary_heap.remove()
        binary_heap.heap_sort()
        binary_heap.display_heap(screen, font)
        priority_text = verify_empty_heap(binary_heap, step)
        priority_surface = font.render(priority_text, True, (255, 255, 255))
        screen.blit(priority_surface, (20, 20))
        pygame.display.flip()
        
        pygame.time.delay(wait_time)

    pygame.quit()
