# ASSIGNMET-3 PYGAME

import pygame
import numpy as np
import random

# Constants
WIDTH, HEIGHT = 1280, 720
GRID_SIZE = 50
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 10

# Initialize grid randomly
grid = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE))

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cloud Assignment-3")

def get_neighbors(x, y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                neighbors.append(grid[nx, ny])
    return neighbors

def update_grid():
    new_grid = np.copy(grid)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            neighbors = get_neighbors(i, j)
            live_neighbors = sum(neighbors)
            if grid[i, j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if live_neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

def draw_grid():
    screen.fill((0, 0, 0))
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = ( 0, 153, 204) if grid[i, j] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main game loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid = update_grid()
    draw_grid()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
