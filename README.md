# Color Grid Generator

A set of Python scripts that generate dynamic color grids using Pygame.

## Features

- **Dynamic Grids**: Generates grids of various shapes including squares, hexagons, and triangles.
- **Random Colors**: Each cell in the grid is assigned a random color every frame (or selected from a specific palette).
- **Interactive Visualization**: Watch the patterns change in real-time.

## Scripts

- `color_grid_square.py`: Generates a grid of squares with full RGB random colors.
- `color_grid_square_rgb.py`: Generates a grid of squares using only pure Red, Green, and Blue colors.
- `color_grid_hexagon.py`: Generates a beautiful hexagonal tiling pattern.
- `color_grid_triangle.py`: Generates a triangular grid pattern.

## Prerequisites

You need Python 3.x and the following libraries installed:

- `pygame`

You can install them using pip:

```bash
pip install pygame
```

## How to Run

Simply run any of the Python scripts:

```bash
python color_grid_square.py
```

Replace `color_grid_square.py` with any of the other filenames to see different patterns.

## Controls

- Close the window to exit the application.

## How it Works

1. **Rendering**: The scripts use Pygame to draw shapes in a grid.
2. **Color Selection**: Colors are generated randomly for each shape in every frame.
