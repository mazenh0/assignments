
from matplotlib import pyplot as plt

def view_grid(grid: list, frame_delay: float, step_number: int) -> None:
    """
    Shows an image of the current state of the grid.
    Parameters:
        grid - list-of-lists representing the current grid. Inner lists use 0s for dead cells, and 1s for live cells.
        frame_delay - the program will pause for this many seconds after displaying the image. 0.1s gives a good animation effect.
        step_number - the step number of the supplied grid (will be displayed above the image).
    """
    if len(grid) == 0:
        raise Exception("Grid is empty")
    
    row_lengths = set([len(row) for row in grid])
    if len(row_lengths) != 1:
        raise Exception(f"Not all grid rows are the same length. Found lengths: {row_lengths}")
    
    if not all([set(row) <= {0, 1} for row in grid]):
        raise Exception("Only 0 and 1 are allowed in thegrid")
    
    plt.cla()
    plt.imshow(grid, cmap='Greys', interpolation='none')
    plt.title(f'Step {step_number}')
    plt.pause(frame_delay)

def read_grid(input_filename: str) -> list:
    """Reads the grid from a file."""
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    grid = []
    for line in lines[1:-1]:  # Skip the border lines
        row = [1 if char == '█' else 0 for char in line.strip()[1:-1]]
        grid.append(row)
    return grid

def write_grid(output_filename: str, grid: list) -> None:
    """Writes the grid to a file."""
    with open(output_filename, 'w', encoding='utf-8') as f:
        border = '▓' * (len(grid[0]) + 2)
        f.write(border + '\n')
        for row in grid:
            row_str = ''.join('█' if cell == 1 else ' ' for cell in row)
            f.write(f'▓{row_str}▓\n')
        f.write(border)

def count_live_neighbors(grid: list, row: int, col: int) -> int:
    """Counts live neighbors around a cell."""
    directions = [
        (-1, -1), (-1, 0), (-1, 1), 
        (0, -1),         (0, 1), 
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            count += grid[r][c]
    return count

def next_state(grid: list) -> list:
    """Computes the next state of the grid."""
    new_grid = []
    for r in range(len(grid)):
        new_row = []
        for c in range(len(grid[0])):
            live_neighbors = count_live_neighbors(grid, r, c)
            if grid[r][c] == 1:  # Alive
                if live_neighbors in (2, 3):
                    new_row.append(1)  # Survive
                else:
                    new_row.append(0)  # Death
            else:  # Dead
                if live_neighbors == 3:
                    new_row.append(1)  # Birth
                else:
                    new_row.append(0)  # Remain Dead
        new_grid.append(new_row)
    return new_grid

def main() -> None:
    """
    Main function that prompts the user for file names and display preference.
    """
    input_filename = input("Enter the name of the input file: ")
    output_filename = input("Enter the name of the output file: ")
    display_response = input("Do you want to display the grid animations? (yes/no): ")
    display = display_response.strip().lower() == 'yes'

    grid = read_grid(input_filename)
    steps = 100

    for step in range(steps):
        if display:
            view_grid(grid, 0.1, step)
        grid = next_state(grid)
    
    write_grid(output_filename, grid)

main()
