import time


# Define the color for the number
blue = (0, 0, 255)

# Number pixel coordinates
number_pixels = [
    [(0,0), (1,0), (2,0), (0,1), (0,2), (0,3), (0,4), (1,4), (2,4), (2,3), (2,2), (2,1)], #0
    [(0, 0), (0, 1), (0, 2), (0, 3),(0, 4)], #1
    [(0,0), (1,0),(2,2), (2,1),(2,0), (0,2), (1,2), (0,3), (0,4), (1,4), (2,4)], #2
    [(0,0), (1,0),(2,0), (2, 1), (2, 2), (2, 3), (2,4), (0,4), (1,4), (2,4), (0,2), (1,2)], #3
    [(0, 0), (0, 1), (0, 2), (2, 0), (2, 1), (2, 2), (2, 3),(2, 4), (1,2)], #4
    [(0,0), (1,0),(2,0), (0,1), (0,2), (1,2), (2,2), (2,3), (2,4), (1,4),(0,4)], #5
    [(0,0), (1,0),(2,0), (0,1), (0,2), (1,2), (2,2), (2,3), (2,4), (1,4),(0,4), (0,3)], #6
    [(2, 0), (2, 1), (2, 2), (2, 3),(2, 4), (1,0), (0,0)], #7
    [(0,0), (1,0),(2,0), (0,1), (0,2), (1,2), (2,2), (2,3), (2,4), (1,4),(0,4), (0,3), (2, 1)], #8
    [(0,0), (1,0),(2,0), (0,1), (0,2), (1,2), (2,2), (2,3), (2,4), (1,4),(0,4), (2, 1)], #9
]

matrix = 0 * 64  # Default matrix (black)
# Function to display a number on the Sense HAT
def display_number(num):
    
    # Set the pixels for the given number
    for x, y in number_pixels[num]:
        index = (y+3) * 8 + x
        matrix[index] = 1
    

display_number(1)
print(matrix)
