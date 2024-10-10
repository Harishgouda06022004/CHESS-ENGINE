import pygame

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 600
screen = pygame.display.set_mode((width, height))  # Set window size
pygame.display.set_caption("Chess Board")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
highlight_color = (173, 216, 230)

# Board settings
rows, cols = 8, 8
square_size = width // cols

# Load and scale images for pieces
white_queen = pygame.image.load("file (8).png")
black_queen = pygame.image.load("file (9).png")
piece_size = (square_size, square_size)
white_queen = pygame.transform.scale(white_queen, piece_size)
black_queen = pygame.transform.scale(black_queen, piece_size)

# Initialize the positions of the queens
board = [[None] * 8 for _ in range(8)]
white_queens = [(7, 3)]
black_queens = [(0, 3)]

def chessboard():
    """Draw the chessboard."""
    for row in range(rows):
        for col in range(cols):
            x = col * square_size
            y = row * square_size
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))

def place_piece():
    """Place queens on the board."""
    for pos in white_queens:
        row, col = pos
        screen.blit(white_queen, (col * square_size, row * square_size))
    for pos in black_queens:
        row, col = pos
        screen.blit(black_queen, (col * square_size, row * square_size))

def highlight_moves(valid_moves):
    """Highlight valid moves for selected piece."""
    for move in valid_moves:
        row, col = move
        x = col * square_size
        y = row * square_size
        pygame.draw.rect(screen, highlight_color, (x, y, square_size, square_size))

def valid_queen_moves(row, col, own_pieces, opponent_pieces):
    """Calculate valid moves for queens by combining rook and bishop moves."""
    valid_moves = []
    
    # Queen moves like a rook (horizontal and vertical)
    for r in range(rows):
        if r != row:
            valid_moves.append((r, col))  # Vertical movement
    for c in range(cols):
        if c != col:
            valid_moves.append((row, c))  # Horizontal movement
    
    # Queen moves like a bishop (diagonal)
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonal directions
    for direction in directions:
        d_row, d_col = direction
        new_row, new_col = row + d_row, col + d_col
        
        while 0 <= new_row < rows and 0 <= new_col < cols:
            if board[new_row][new_col] is None:  # Empty square
                valid_moves.append((new_row, new_col))
            elif (new_row, new_col) in opponent_pieces:  # Capture opponent's piece
                valid_moves.append((new_row, new_col))
                break
            else:  # Blocked by own piece
                break
            
            new_row += d_row
            new_col += d_col

    # Remove moves blocked by own pieces
    valid_moves = [move for move in valid_moves if move not in own_pieces]
    
    return valid_moves

running = True
selected = False
valid_moves = []
selected_queen = None
selected_color = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_col = mouse_x // square_size
            clicked_row = mouse_y // square_size
            clicked_pos = (clicked_row, clicked_col)

            # Select the queen if it's clicked
            if clicked_pos in white_queens or clicked_pos in black_queens:
                selected_queen = clicked_pos
                selected_color = "white" if clicked_pos in white_queens else "black"
                
                # Calculate valid moves for the selected queen
                if selected_color == "white":
                    valid_moves = valid_queen_moves(clicked_row, clicked_col, white_queens, black_queens)
                else:
                    valid_moves = valid_queen_moves(clicked_row, clicked_col, black_queens, white_queens)

                selected = True  # Mark as selected
            else:
                # Move the selected queen if there are valid moves
                if selected and clicked_pos in valid_moves:
                    if selected_color == "white":
                        white_queens.remove(selected_queen)
                        white_queens.append(clicked_pos)
                    elif selected_color == "black":
                        black_queens.remove(selected_queen)
                        black_queens.append(clicked_pos)
                    # Deselect after moving
                    selected = False
                    valid_moves = []
                    selected_queen = None
                    selected_color = None

    screen.fill(black)
    chessboard()
    place_piece()

    # Highlight valid moves if a piece is selected
    if selected:
        highlight_moves(valid_moves)

    pygame.display.flip()

pygame.quit()
