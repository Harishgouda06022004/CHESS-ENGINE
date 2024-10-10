# CHESS-ENGINE
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

# Load pieces
white_pawn = pygame.image.load("file.png")
black_pawn = pygame.image.load("file (1).png")
white_rook = pygame.image.load("file (3).png")
black_rook = pygame.image.load("file (2).png")
white_knight = pygame.image.load("file (12).png")
black_knight = pygame.image.load("file (5).png")
white_bishop = pygame.image.load("file (7).png")
black_bishop = pygame.image.load("file (6).png")
white_queen = pygame.image.load("file (8).png")
black_queen = pygame.image.load("file (9).png")
white_king = pygame.image.load("file (10).png")
black_king = pygame.image.load("file (11).png")
piece_size = (square_size, square_size)
white_pawn = pygame.transform.scale(white_pawn, piece_size)
black_pawn = pygame.transform.scale(black_pawn, piece_size)
white_rook = pygame.transform.scale(white_rook, piece_size)
black_rook = pygame.transform.scale(black_rook, piece_size)
white_knight = pygame.transform.scale(white_knight, piece_size)
black_knight = pygame.transform.scale(black_knight, piece_size)
white_bishop = pygame.transform.scale(white_bishop, piece_size)
black_bishop = pygame.transform.scale(black_bishop, piece_size)
white_queen = pygame.transform.scale(white_queen, piece_size)
black_queen = pygame.transform.scale(black_queen, piece_size)
white_king = pygame.transform.scale(white_king, piece_size)
black_king = pygame.transform.scale(black_king, piece_size)

# Initialize board
board = [[None] * 8 for _ in range(8)]
board[1] = ['bp'] * 8  # Black pawns on row 1
board[6] = ['wp'] * 8  # White pawns on row 6
white_rooks = [(7, 0), (7, 7)]  # Positions of white rooks
black_rooks = [(0, 0), (0, 7)]
white_knights = [(7, 1), (7, 6)]  # Positions of white knights
black_knights = [(0, 1), (0, 6)]  # Positions of black knights
white_bishops=[(7,2),(7,5)]
black_bishops=[(0,2),(0,5)]
white_queens=[(7,3)]
black_queens=[(0,3)]
white_kings = [(7,4)]
black_kings = [(0,4)]

# Knight movement pattern
knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# Drawing the chessboard
def chessboard():
    """Draw the chessboard."""
    for row in range(rows):
        for col in range(cols):
            x = col * square_size
            y = row * square_size
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))

# Placing the pieces
def place_piece():
    """Place the pawns, rooks, and knights on the board."""
    for row in range(rows):
        for col in range(cols):
            piece = board[row][col]
            if piece == 'wp':
                screen.blit(white_pawn, (col * square_size, row * square_size))
            elif piece == 'bp':
                screen.blit(black_pawn, (col * square_size, row * square_size))
    for pos in white_rooks:
        row, col = pos
        screen.blit(white_rook, (col * square_size, row * square_size))
    for pos in black_rooks:
        row, col = pos
        screen.blit(black_rook, (col * square_size, row * square_size))
    # Place knights
    for pos in white_knights:
        row, col = pos
        screen.blit(white_knight, (col * square_size, row * square_size))

    for pos in black_knights:
        row, col = pos
        screen.blit(black_knight, (col * square_size, row * square_size))
    # place bishops
    for pos in white_bishops:
        row,col=pos
        screen.blit(white_bishop,(col*square_size,row*square_size))
    for pos in black_bishops:
        row,col=pos
        screen.blit(black_bishop,(col*square_size,row*square_size))
    # place queens
    for pos in white_queens:
        row,col=pos
        screen.blit(white_queen,(col*square_size,row*square_size))
    for pos in black_queens:
        row,col=pos
        screen.blit(black_queen,(col*square_size,row*square_size))
    #place Kings
    for pos in white_kings:
        row,col=pos
        screen.blit(white_king,(col*square_size,row*square_size))
    for pos in black_kings:
        row,col=pos
        screen.blit(black_king,(col*square_size,row*square_size))

# Highlight valid moves for selected pieces
def highlight_moves(valid_moves):
    """Highlight valid moves for selected piece."""
    for move in valid_moves:
        row, col = move
        x = col * square_size
        y = row * square_size
        pygame.draw.rect(screen, highlight_color, (x, y, square_size, square_size))

# Valid pawn moves
def valid_pawn_moves(row, col, piece):
    """Calculate valid moves for pawns."""
    moves = []
    if piece == 'wp':  # White pawn movement
        if row > 0 and board[row - 1][col] is None:  # Move 1 step forward
            moves.append((row - 1, col))
        if row == 6 and board[row - 1][col] is None and board[row - 2][col] is None:  # 2 steps from start
            moves.append((row - 2, col))
        if row > 0 and col > 0 and board[row - 1][col - 1] == 'bp':  # Capture left
            moves.append((row - 1, col - 1))
        if row > 0 and col < cols - 1 and board[row - 1][col + 1] == 'bp':  # Capture right
            moves.append((row - 1, col + 1))

    elif piece == 'bp':  # Black pawn movement
        if row < rows - 1 and board[row + 1][col] is None:  # Move 1 step forward
            moves.append((row + 1, col))
        if row == 1 and board[row + 1][col] is None and board[row + 2][col] is None:  # 2 steps from start
            moves.append((row + 2, col))
        if row < rows - 1 and col > 0 and board[row + 1][col - 1] == 'wp':  # Capture left
            moves.append((row + 1, col - 1))
        if row < rows - 1 and col < cols - 1 and board[row + 1][col + 1] == 'wp':  # Capture right
            moves.append((row + 1, col + 1))
    
    return moves

# Valid rook moves
def calculate_rook_moves(start_row, start_col, own_rooks, opponent_rooks):
    """Calculate valid moves for rooks."""
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

# Valid knight moves
def get_valid_knight_moves(pos):
    """Calculate valid moves for knights."""
    row, col = pos
    valid_moves = []
    for move in knight_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < rows and 0 <= new_col < cols:  # Boundary check
            if board[new_row][new_col] is None or board[new_row][new_col] != board[row][col]:  # Check if empty or opponent's piece
                valid_moves.append((new_row, new_col))
    return valid_moves
# Valid bishop moves
def valid_bishop_moves(row, col, own_bishops, opponent_pieces):
    """Calculate valid moves for bishops."""
    valid_moves = []
    
    # Diagonal moves: top-left, top-right, bottom-left, bottom-right
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
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

    return valid_moves
# queen moves
# Valid queen moves
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
#king moves function
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


# Move rook to a new position
def move_rook(rook_pos, new_pos, rooks_list):
    """Move a rook to a new valid position."""
    if rook_pos in rooks_list:
        rooks_list.remove(rook_pos)
        rooks_list.append(new_pos)

# Move knight to a new position
def move_knight(knight_pos, new_pos, knights_list):
    """Move a knight to a new valid position."""
    if knight_pos in knights_list:
        knights_list.remove(knight_pos)
        knights_list.append(new_pos)

# Main game loop
running = True
selected = False
valid_moves = []
selected_piece = None
selected_pos = None
selected_rook = None
selected_knight = None
selected_bishop=None
selected_queen=None
selected_king=None
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

            # Handle piece selection and movement
            if not selected:
                selected_piece = board[clicked_row][clicked_col]
                selected_pos = (clicked_row, clicked_col)

                if selected_piece in ['wp', 'bp']:  # Pawn selected
                    valid_moves = valid_pawn_moves(clicked_row, clicked_col, selected_piece)
                    selected = True
                elif clicked_pos in white_rooks or clicked_pos in black_rooks:  # Rook selected
                    if clicked_pos in white_rooks:
                        selected_rook = clicked_pos
                        selected_color = "white"
                        valid_moves = calculate_rook_moves(clicked_row, clicked_col, white_rooks, black_rooks)
                    elif clicked_pos in black_rooks:
                        selected_rook = clicked_pos
                        selected_color = "black"
                        valid_moves = calculate_rook_moves(clicked_row, clicked_col, black_rooks, white_rooks)
                    selected = True
                elif clicked_pos in white_knights or clicked_pos in black_knights:  # Knight selected
                    if clicked_pos in white_knights:
                        selected_knight = clicked_pos
                        selected_color = "white"
                        valid_moves = get_valid_knight_moves(clicked_pos)
                    elif clicked_pos in black_knights:
                        selected_knight = clicked_pos
                        selected_color = "black"
                        valid_moves = get_valid_knight_moves(clicked_pos)
                    selected = True
                elif clicked_pos in white_bishops or clicked_pos in black_bishops:  # Bishop selected
                    if clicked_pos in white_bishops:
                        selected_bishop = clicked_pos
                        selected_color = "white"
                        valid_moves = valid_bishop_moves(clicked_row, clicked_col, white_bishops, black_bishops + black_knights + black_rooks)
                    elif clicked_pos in black_bishops:
                        selected_bishop = clicked_pos
                        selected_color = "black"
                        valid_moves = valid_bishop_moves(clicked_row, clicked_col, black_bishops, white_bishops + white_knights + white_rooks)
                    selected = True
                # Select the queen if it's clicked
                elif clicked_pos in white_queens or clicked_pos in black_queens:
                    selected_queen = clicked_pos
                    selected_color = "white" if clicked_pos in white_queens else "black"
                    
                    # Calculate valid moves for the selected queen
                    if selected_color == "white":
                        valid_moves = valid_queen_moves(clicked_row, clicked_col, white_queens, black_queens)
                    else:
                        valid_moves = valid_queen_moves(clicked_row, clicked_col, black_queens, white_queens)

                    selected = True  # Mark as selected
                elif clicked_pos in white_kings or clicked_pos in black_kings:
                    selected_king = clicked_pos
                    selected_color = "white" if clicked_pos in white_kings else "black"
                    
                    # Calculate valid moves for the selected queen
                    if selected_color == "white":
                        valid_moves = valid_king_moves(clicked_row, clicked_col, white_kings, black_kings)
                    else:
                        valid_moves = valid_king_moves(clicked_row, clicked_col, black_kings, white_kings)

                    selected = True  # Mark as selected

            else:
                # Move the selected piece (pawn, rook, or knight)
                if (clicked_row, clicked_col) in valid_moves:
                    if selected_piece in ['wp', 'bp']:  # Move pawn
                        board[clicked_row][clicked_col] = selected_piece
                        board[selected_pos[0]][selected_pos[1]] = None
                    elif selected_rook is not None:  # Move rook
                        if selected_color == "white":
                            move_rook(selected_rook, clicked_pos, white_rooks)
                        elif selected_color == "black":
                            move_rook(selected_rook, clicked_pos, black_rooks)
                    elif selected_knight is not None:  # Move knight
                        if selected_color == "white":
                            move_knight(selected_knight, clicked_pos, white_knights)
                        elif selected_color == "black":
                            move_knight(selected_knight, clicked_pos, black_knights)
                    elif selected_bishop is not None:  # Move bishop
                        if selected_color == "white":
                            white_bishops.remove(selected_bishop)
                            white_bishops.append(clicked_pos)
                        elif selected_color == "black":
                            black_bishops.remove(selected_bishop)
                            black_bishops.append(clicked_pos)
                    elif selected_queen is not None:  # Move queen
                        if selected_color == "white":
                            white_queens.remove(selected_queen)
                            white_queens.append(clicked_pos)
                        elif selected_color == "black":
                            black_queens.remove(selected_queen)
                            black_queens.append(clicked_pos)
                    elif selected_king is not None:  # Move queen
                        if selected_color == "white":
                            white_kings.remove(selected_king)
                            white_kings.append(clicked_pos)
                        elif selected_color == "black":
                            black_kings.remove(selected_king)
                            black_kings.append(clicked_pos)
                    
                    # Deselect after moving
                    selected = False
                    valid_moves = []
                    selected_piece = None
                    selected_rook = None
                    selected_knight = None
                    selected_bishop=None
                    selected_queen=None
                    selected_king=None
                    selected_color = None

    # Draw the board and pieces
    screen.fill(black)
    chessboard()
    place_piece()

    # Highlight valid moves if a piece is selected
    if selected:
        highlight_moves(valid_moves)

    pygame.display.flip()

pygame.quit()
