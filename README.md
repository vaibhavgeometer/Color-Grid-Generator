# Color Grid Generator

A set of Python scripts that generate dynamic color grids using Pygame and produce real-time sound based on the colors displayed.

## Features

- **Dynamic Grids**: Generates grids of various shapes including squares, hexagons, and triangles.
- **Random Colors**: Each cell in the grid is assigned a random color every frame (or selected from a specific palette).
- **Sound Synthesis**: Generates a unique audio tone for each frame based on the average Red, Green, and Blue values of all cells.
- **Interactive Visualization**: Watch the patterns change and listen to the corresponding soundscapes.

## Scripts

- `color_grid_square.py`: Generates a grid of squares with full RGB random colors.
- `color_grid_square_rgb.py`: Generates a grid of squares using only pure Red, Green, and Blue colors.
- `color_grid_hexagon.py`: Generates a beautiful hexagonal tiling pattern.
- `color_grid_triangle.py`: Generates a triangular grid pattern.

## Prerequisites

You need Python 3.x and the following libraries installed:

- `pygame`
- `numpy`

You can install them using pip:

```bash
pip install pygame numpy
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
3. **Audio Generation**: 
   - The average Red, Green, and Blue values of all shapes in the current frame are calculated.
   - These averages are mapped to specific frequency ranges:
     - **Red**: Low frequencies (Bass)
     - **Green**: Mid frequencies
     - **Blue**: High frequencies
   - Sine waves are generated for each frequency, mixed together, and played using Pygame's mixer.
