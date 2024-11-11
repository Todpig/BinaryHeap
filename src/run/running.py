import pygame
from src.utils import verify_empty_heap
from src.binary_heap.binary_heap import BinaryHeap
from src.utils import wait_time

class Run:
    def __init__(self, array_values: list, question: int, values: dict):
        self.binary_heap = BinaryHeap()
        self.array_values = array_values
        self.question = question
        self.values = values
        pygame.init()
        screen_width, screen_height = 1280, 720
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Binary Heap Tree Visualization")
        self.font = pygame.font.SysFont(None, 36)

    def step_one(self):
        for value in self.array_values:
            self.binary_heap.insert(value)
            self.binary_heap.display_heap(self.screen, self.font)
            priority_text = verify_empty_heap(self.binary_heap, self.question)
            priority_surface = self.font.render(priority_text, True, (255, 255, 255))
            self.screen.blit(priority_surface, (20, 20))
            pygame.display.flip()
            pygame.time.delay(wait_time)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        pygame.time.delay(wait_time)

    def step_two(self):
        for index in list(self.values.keys()):
            self.binary_heap.change_priority(index, self.values[index])
            self.binary_heap.display_heap(self.screen, self.font)
            priority_text = verify_empty_heap(self.binary_heap, self.question)
            priority_surface = self.font.render(priority_text, True, (255, 255, 255))
            self.screen.blit(priority_surface, (20, 20))
            pygame.display.flip()
            pygame.time.delay(wait_time)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            pygame.time.delay(wait_time)

    def step_three(self):     
        for _ in range(5):
            self.binary_heap.remove()
            self.binary_heap.display_heap(self.screen, self.font)
            priority_text = verify_empty_heap(self.binary_heap, self.question)
            priority_surface = self.font.render(priority_text, True, (255, 255, 255))
            self.screen.blit(priority_surface, (20, 20))
            pygame.display.flip()
            pygame.time.delay(wait_time)


    def step_four(self):
        for _ in range(self.binary_heap.size):
            self.binary_heap.remove()
            self.binary_heap.heap_sort()
            self.binary_heap.display_heap(self.screen, self.font)
            priority_text = verify_empty_heap(self.binary_heap, self.question)
            priority_surface = self.font.render(priority_text, True, (255, 255, 255))
            self.screen.blit(priority_surface, (20, 20))
            pygame.display.flip()
            pygame.time.delay(wait_time)




















def second_set_of_numbers(binary_heap: BinaryHeap):


    # Step 3: Remove five elements from the heap
   

    # Step 4: Heapsort
    

    pygame.quit()