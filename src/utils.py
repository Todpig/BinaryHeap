import pygame
from src.binary_heap.binary_heap import BinaryHeap

wait_time = 500


def draw_heap(binary_heap: BinaryHeap, screen, font):
        binary_heap.display_heap(screen, font)
        priority_text = f"Highest Priority: {binary_heap.heap[1]}"
        priority_surface = font.render(priority_text, True, (255, 255, 255))
        screen.blit(priority_surface, (20, 20))
        pygame.display.flip()
        pygame.time.delay(wait_time)