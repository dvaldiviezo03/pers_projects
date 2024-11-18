# todo: Board - DONE
board = [
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
]

# number each row and column, get from (0,0) -> a8, b8, c8, etc. - DONE
def board_coordinates(board):
    columns = ['a','b','c','d','e','f','g','h']
    print(" ",end = "")
    for col in columns:
        print(" " + col, end = " ")
    print()
    for i, row in enumerate(board):
        print(8-i, end = ": ")
        for piece in row:
            print(piece, end = " ")
        print()

board_coordinates(board)

# todo: Turns
# todo: Move pieces
def move_piece(board, start, end):
    start_row, start_col = start
    end_row, end_col = end

white_piece_loc = {
    "wP": [[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[6,8]],
    "wR": [[7,1],[7,8]],
    "wN": [[7,2],[7,7]],
    "wB": [[7,3],[7,6]],
    "wQ": [[7,4]],
    "wK": [[7,5]]
}

black_piece_loc = {

}

# todo: Check for valid move
def is_valid_move(board, start, end):
    return

# todo: Check for checkmate
def is_checkmate(board, start, end):
    return