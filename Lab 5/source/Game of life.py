import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100
ON = 255
OFF = 0
vals = [ON, OFF]
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def update(data):
  global grid

  newGrid = grid.copy()
  for i in range(N):
    for j in range(N):

      total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
               grid[(i-1)%N, j] + grid[(i+1)%N, j] +
               grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
               grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255

      if grid[i, j]  == ON:
        if (total < 2) or (total > 3):
          newGrid[i, j] = OFF
      else:
        if total == 3:
          newGrid[i, j] = ON

  mat.set_data(newGrid)
  grid = newGrid
  return [mat]


fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=150,
                              save_count=150)
plt.show()