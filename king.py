import pygame

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600  # Chessboard size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Board")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
highlight_color = (173, 216, 230) # Light blue for highlighting valid moves

# Chessboard parameters
rows, cols = 8, 8  # 8x8 grid for the chessboard
square_size = width // cols  # Calculate size of each square
white_king = pygame.image.load("file (10).png")
black_king = pygame.image.load("file (11).png")
piecesize=(square_size,square_size)
white_king = pygame.transform.scale(white_king, piecesize)
black_king = pygame.transform.scale(black_king, piecesize)
board = [[None] * 8 for _ in range(8)]
white_kings = [(7,4)]
black_kings = [(0,4)]
def chessboard():
    """Draw the chessboard."""
    for row in range(rows):
        for col in range(cols):
            x = col * square_size
            y = row * square_size
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))
def place_piece():
    for pos in white_kings:
        row,col=pos
        screen.blit(white_king,(col*square_size,row*square_size))
    for pos in black_kings:
        row,col=pos
        screen.blit(black_king,(col*square_size,row*square_size))
def highlight_moves(valid_moves):
    """Highlight valid moves for selected piece."""
    for move in valid_moves:
        row, col = move
        x = col * square_size
        y = row * square_size
        pygame.draw.rect(screen, highlight_color, (x, y, square_size, square_size))
def valid_king_moves(row, col, current_kings, opponent_kings):
    """Calculate valid king moves for the selected king."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    valid_moves = []
    
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        
        if 0 <= new_row < rows and 0 <= new_col < cols:  # Stay within the board boundaries
            new_pos = (new_row, new_col)
            
            # Ensure the king doesn't move onto a square occupied by another king of the same color
            if new_pos not in current_kings:
                valid_moves.append(new_pos)

    return valid_moves

running = True
selected = False
valid_moves = []
selected_piece = None
selected_pos = None
selected_king = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_col = mouse_x // square_size
            clicked_row = mouse_y // square_size
            clicked_pos = (clicked_row, clicked_col)
            if clicked_pos in white_kings or clicked_pos in black_kings:
                    selected_queen = clicked_pos
                    selected_color = "white" if clicked_pos in white_kings else "black"
                    
                    # Calculate valid moves for the selected queen
                    if selected_color == "white":
                        valid_moves = valid_king_moves(clicked_row, clicked_col, white_kings, black_kings)
                    else:
                        valid_moves = valid_king_moves(clicked_row, clicked_col, black_kings, white_kings)

                    selected = True  # Mark as selected
            else:
                if selected_queen is not None:  # Move queen
                        if selected_color == "white":
                            white_kings.remove(selected_queen)
                            white_kings.append(clicked_pos)
                        elif selected_color == "black":
                            black_kings.remove(selected_queen)
                            black_kings.append(clicked_pos)
                    # Deselect after moving
                        selected = False
                        valid_moves = []
                        selected_piece = None
                        selected_king = None
                        selected_color=None
    screen.fill(black)
    chessboard()
    place_piece()

    # Highlight valid moves if a piece is selected
    if selected:
        highlight_moves(valid_moves)

    pygame.display.flip()

pygame.quit()
