# Image Manipulation Patterns

This directory contains various Python scripts that generate different image patterns using OpenCV and NumPy. Below is a summary of each script and the process it follows to create the respective patterns.

## Files and Descriptions

### 1. `border_color_pattern.py`
This script creates a 500x500 white image and adds a randomly colored border around it.

**Process:**
- Create a white image of size 500x500.
- Generate a random color.
- Apply the color to the top, bottom, left, and right borders of the image.
- Display the image.

### 2. `charuco_board_pattern.py`
This script generates a ChArUco board pattern using OpenCV's `aruco` module.

**Process:**
- Define the ChArUco board parameters.
- Create the ChArUco board.
- Draw the ChArUco board on an image.
- Display the image.

### 3. `chess_board.py`
This script generates a chessboard pattern.

**Process:**
- Define the chessboard size.
- Create the chessboard pattern.
- Draw the chessboard on an image.
- Display the image.

### 4. `diagonal_checkbox_in_color_image.py`
This script creates a 500x500 white image and fills the diagonal checkboxes with random colors.

**Process:**
- Create a white image of size 500x500.
- Iterate through a 10x10 grid.
- For each cell on the diagonals, generate a random color and fill the cell with that color.
- Display the image.

### 5. `diamond_color_pattern.py`
This script generates a diamond pattern with random colors.

**Process:**
- Create a white image.
- Define the diamond shape and size.
- Fill the diamond shapes with random colors.
- Display the image.

### 6. `hour_glass.py`
This script generates an hourglass pattern.

**Process:**
- Create a white image.
- Define the hourglass shape and size.
- Fill the hourglass shapes with random colors.
- Display the image.

### 7. `make_circle_pattern.py`
This script creates a pattern of circles on a black background.

**Process:**
- Create a black image of size 600x600.
- Define a function to draw a circle on the image.
- Iterate through a 5x5 grid.
- For each cell, draw a circle if the sum of the row and column indices is even.
- Display the image.

### 8. `mat_mul.py`
This script performs matrix multiplication on two matrices.

**Process:**
- Define two matrices.
- Perform matrix multiplication.
- Display the result.

### 9. `time_on_canvas.py`
This script displays the current time on a canvas.

**Process:**
- Create a white image.
- Get the current time.
- Draw the time on the image.
- Display the image.

### 10. `traingle_color_pattern.py`
This script creates a 500x500 white image and fills the lower triangle with random colors.

**Process:**
- Create a white image of size 500x500.
- Iterate through a 10x10 grid.
- For each cell in the lower triangle, generate a random color and fill the cell with that color.
- Display the image.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## How to Run

To run any of the scripts, use the following command:

```bash
python <script_name>.py
```

For example, to run the `border_color_pattern.py` script:

```bash
python border_color_pattern.py
```

## License

This project is licensed under the MIT License.