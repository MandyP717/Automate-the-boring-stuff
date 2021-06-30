"""
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g':'bbischip'}
to represent a chess board. Write a function named is_Valid_Chess_Board() that takes a dictionary
argument and return True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces, at most 8 pawns and all pieces must be on a valid space.
The pieces names begin with either a 'w' or 'b' to represent white or black, followed by piece name.
"""

example_board = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbischip",
    "5h": "bqueen",
    "3e": "wking",
}


def is_Valid_Chess_Board(dic):
    black_pieces = {}
    white_pieces = {}
    valid_board = [
        "a1",
        "a2",
        "a3",
        "a4",
        "a5",
        "a6",
        "a7",
        "a8",
        "b1",
        "b2",
        "b3",
        "b4",
        "b5",
        "b6",
        "b7",
        "b8",
        "c1",
        "c2",
        "c3",
        "c4",
        "c5",
        "c6",
        "c7",
        "c8",
        "d1",
        "d2",
        "d3",
        "d4",
        "d5",
        "d6",
        "d7",
        "d8",
        "e1",
        "e2",
        "e3",
        "e4",
        "e5",
        "e6",
        "e7",
        "e8",
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "g1",
        "g2",
        "g3",
        "g4",
        "g5",
        "g6",
        "g7",
        "g8",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "h7",
        "h8",
    ]

    for key, value in dic.items():  # seperate the pieces in white/black
        if value[0] == "b":
            black_pieces[key] = value
        elif value[0] == "w":
            white_pieces[key] = value

    only_piece_name_black = list(black_pieces.values())
    only_piece_name_white = list(white_pieces.values())

    if (
        len(black_pieces) <= 16 and len(white_pieces) <= 16
    ):  # check is only 16 pieces for white and black
        if (
            only_piece_name_black.count("bking") == 1
            and only_piece_name_white.count("wking") == 1
        ):  # only one king
            if (
                only_piece_name_black.count("bpawn") <= 8
                and only_piece_name_white.count("wpawn") <= 8
            ):  # 8 or less pawns
                return True
    else:
        return False


print(is_Valid_Chess_Board(example_board))
