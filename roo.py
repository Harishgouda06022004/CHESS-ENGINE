import pygame

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600  # Chessboard size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Board")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (173, 216, 230)  # Light blue for highlighting valid moves

# Chessboard parameters
rows, cols = 8, 8  # 8x8 grid for the chessboard
square_size = width // cols  # Calculate size of each square
white_rooks = [(7, 0), (7, 7)]
black_rooks = [(0, 0), (0, 7)]

# Load rook images and resize
white_rook = pygame.image.load("file (3).png")
black_rook = pygame.image.load("file (2).png")
piecesize = (square_size, square_size)
white_rook = pygame.transform.scale(white_rook, piecesize)
black_rook = pygame.transform.scale(black_rook, piecesize)

# Chessboard function to draw squares
def chess_board():
    for row in range(rows):
        for col in range(cols):
            x = col * square_size
            y = row * square_size
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))

# Function to place pieces (rooks)
def place_pieces():
    for pos in white_rooks:
        row, col = pos
        screen.blit(white_rook, (col * square_size, row * square_size))

    for pos in black_rooks:
        row, col = pos
        screen.blit(black_rook, (col * square_size, row * square_size))

# Function to calculate valid rook moves (horizontal and vertical)
def calculate_rook_moves(start_row, start_col, own_rooks, opponent_rooks):
    valid_moves = []
    # Vertical moves (up and down)
    for row in range(rows):
        if row != start_row:
            valid_moves.append((row, start_col))
    # Horizontal moves (left and right)
    for col in range(cols):
        if col != start_col:
            valid_moves.append((start_row, col))

    # Remove moves blocked by other rooks
    valid_moves = [move for move in valid_moves if move not in own_rooks and move not in opponent_rooks]
    return valid_moves

# Function to highlight valid moves
def highlight_moves(valid_moves):
    for move in valid_moves:
        row, col = move
        x = col * square_size
        y = row * square_size
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, (x, y, square_size, square_size))

# Function to move the rook
def move_rook(rook_pos, new_pos, rooks_list):
    if rook_pos in rooks_list:
        rooks_list.remove(rook_pos)
        rooks_list.append(new_pos)

running = True
selected = False
selected_rook = None
selected_color = None  # Track whether a white or black rook is selected
valid_moves = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row = mouse_y // square_size
            clicked_col = mouse_x // square_size
            clicked_pos = (clicked_row, clicked_col)

            if not selected:
                # Select a white or black rook
                if clicked_pos in white_rooks:
                    selected_rook = clicked_pos
                    selected_color = "white"
                    valid_moves = calculate_rook_moves(clicked_row, clicked_col, white_rooks, black_rooks)
                    selected = True
                elif clicked_pos in black_rooks:
                    selected_rook = clicked_pos
                    selected_color = "black"
                    valid_moves = calculate_rook_moves(clicked_row, clicked_col, black_rooks, white_rooks)
                    selected = True
            else:
                # Move the rook to a valid move
                if clicked_pos in valid_moves:
                    if selected_color == "white":
                        move_rook(selected_rook, clicked_pos, white_rooks)
                    elif selected_color == "black":
                        move_rook(selected_rook, clicked_pos, black_rooks)
                    selected = False
                    selected_rook = None
                    selected_color = None
                    valid_moves = []
                else:
                    # Deselect the rook if clicked on an invalid square
                    selected = False
                    selected_rook = None
                    selected_color = None
                    valid_moves = []

    screen.fill(BLACK)  # Clear the screen

    chess_board()  # Draw the chessboard

    if selected:
        highlight_moves(valid_moves)  # Highlight valid moves

    place_pieces()  # Place the rooks

    pygame.display.flip()  # Update the display

pygame.quit()

