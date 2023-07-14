# Game of Life: Simulate Conway's Game of Life using NumPy arrays.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulate_game_of_life(initial_state, num_steps):
    height, width = initial_state.shape
    current_state = initial_state.copy()
    next_state = np.zeros((height, width), dtype=int)

    for _ in range(num_steps):
        for i in range(height):
            for j in range(width):
                # Count the number of live neighbors
                num_neighbors = np.sum(current_state[max(0, i-1):min(height, i+2), max(0, j-1):min(width, j+2)]) - current_state[i, j]

                # Apply the rules of the game
                if current_state[i, j] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                    next_state[i, j] = 0
                elif current_state[i, j] == 0 and num_neighbors == 3:
                    next_state[i, j] = 1
                else:
                    next_state[i, j] = current_state[i, j]

        current_state = next_state.copy()

    return current_state

def plot_game_of_life(initial_state, num_steps):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    ax.set_aspect('equal')
    ax.set_xlim(0, initial_state.shape[1])
    ax.set_ylim(0, initial_state.shape[0])

    img = ax.imshow(initial_state, cmap='binary')

    def update(frame):
        img.set_array(simulate_game_of_life(initial_state, frame))
        return img,

    anim = animation.FuncAnimation(fig, update, frames=num_steps, interval=500, blit=True)
    plt.show()

# Test case
initial_state = np.array([[0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0]])

num_steps = 50

plot_game_of_life(initial_state, num_steps)
