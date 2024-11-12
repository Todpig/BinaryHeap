import pygame
from src.binary_heap.binary_heap import BinaryHeap
from src.utils import draw_heap, wait_time

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
            draw_heap(self.binary_heap, self.screen, self.font)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        pygame.time.delay(wait_time)

    def step_two(self):
        for index in list(self.values.keys()):
            self.binary_heap.change_priority(index, self.values[index])
            draw_heap(self.binary_heap, self.screen, self.font)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            pygame.time.delay(wait_time)

    def step_three(self, count: int):     
        for _ in range(count):
            self.binary_heap.remove()
            draw_heap(self.binary_heap, self.screen, self.font)


    def step_four(self):
        new_binary_heap = BinaryHeap(self.binary_heap.heap[1:])
        new_binary_heap.heap_sort(self.screen, self.font)
        pygame.time.delay(wait_time)

    def step_five(self):
        priority_surface = self.font.render(f"Highest Priority is: {self.binary_heap.heap[1]}", True, (255, 255, 255))
        self.screen.blit(priority_surface, (640, 600))
        pygame.display.flip()
        pygame.time.delay(wait_time)

    def quit(self):
        pygame.quit()
        return