import pygame
import math

class BinaryHeap:
    def __init__(self, heap_values: list = []):
        self.heap = [math.inf] + heap_values  
        self.size = len(heap_values)

    def insert(self, value: int):
        self.heap.append(value)
        self.size += 1
        self.heap_up(self.size)

    def arrange(self):  
        for start in range(self.size // 2, 0, -1):
            self.heap_down(start)

    def heap_up(self, start: int):
        parent = start // 2
        if parent >= 1 and self.heap[start] > self.heap[parent]:
            self.heap[start], self.heap[parent] = self.heap[parent], self.heap[start]
            self.heap_up(parent)

    def heap_down(self, start: int, size: int = None):
        if size is None:
            size = self.size
            
        largest = start
        left = 2 * start
        right = 2 * start + 1

        if left <= size and self.heap[left] > self.heap[largest]:
            largest = left
        if right <= size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != start:
            self.heap[start], self.heap[largest] = self.heap[largest], self.heap[start]
            self.heap_down(largest, size)

    def remove(self):
        if self.size != 0:
            last_value = self.heap[self.size]
            self.heap[1] = last_value
            self.size -= 1
            self.heap.pop()
            self.heap_down(1)

    def change_priority(self, start_index: int, new_priority: int):
        old_value = self.heap[start_index]
        self.heap[start_index] = new_priority
        if new_priority > old_value:
            self.heap_up(start_index)
        else:
            self.heap_down(start_index)

    def get_high_priority(self):
        return self.heap[1]

    def heap_sort(self, screen=None, font=None):
        from src.utils import draw_heap
        self.arrange()
        current_size = self.size
        while current_size > 1:
            if screen is not None and font is not None:
                draw_heap(self, screen, font)
            self.heap[1], self.heap[current_size] = self.heap[current_size], self.heap[1]
            current_size -= 1
            self.heap_down(1, current_size)
            pygame.time.delay(1000)
        if screen is not None and font is not None:
            draw_heap(self, screen, font)


    def display_heap(self, screen, font):
        screen.fill((0, 0, 0))
        self.draw_heap_nodes(self.heap[1:], screen, font)
        pygame.display.flip()

    def draw_node(self, value, x, y, radius, screen, font):
        pygame.draw.circle(screen, (255, 255, 255), (x, y), radius)
        text = font.render(str(value), True, (0, 0, 0))
        screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    def draw_heap_nodes(self, arr, screen, font):
        positions = {}
        root_x = 640
        root_y = 50
        level_height = 100
        node_radius = 30

        for i, value in enumerate(arr):
            level = math.floor(math.log2(i + 1))
            index_in_level = i - (2**level - 1) 
            nodes_in_level = 2**level     

            # Cálculo da posição x do nó
            node_x = root_x + (index_in_level - (nodes_in_level - 1) / 2) * (node_radius * 3)
            node_y = root_y + level * level_height  # Cálculo da posição y do nó

            # Desenha a linha de ligação com o nó pai
            if i > 0:
                parent_index = (i - 1) // 2
                parent_x, parent_y = positions[parent_index]
                pygame.draw.line(screen, (255, 255, 255), (parent_x, parent_y), (node_x, node_y), 2)

            positions[i] = (node_x, node_y)
            self.draw_node(value, node_x, node_y, node_radius, screen, font)
