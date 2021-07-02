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
    "1a": "wpawn",
    "2a": "wpawn",
    "3a": "wpawn",
    "4a": "wpawn",
    "5a": "wpawn",
    "6a": "wpawn",
    "7a": "wpawn",
    "8a": "wpawn",
    "2b": "wpawn",
    "3b": "wpawn",
    "5b": "wpawn",
}

valid_board = [
    "1a",
    "1b",
    "1c",
    "1d",
    "1e",
    "1f",
    "1g",
    "1h",
    "2a",
    "2b",
    "2c",
    "2d",
    "2e",
    "2f",
    "2g",
    "2h",
    "3a",
    "3b",
    "3c",
    "3d",
    "3e",
    "3f",
    "3g",
    "3h",
    "4a",
    "4b",
    "4c",
    "4d",
    "4e",
    "4f",
    "4g",
    "4h",
    "5a",
    "5b",
    "5c",
    "5d",
    "5e",
    "5f",
    "5g",
    "5h",
    "6a",
    "6b",
    "6c",
    "6d",
    "6e",
    "6f",
    "6g",
    "6h",
    "7a",
    "7b",
    "7c",
    "7d",
    "7e",
    "7f",
    "7g",
    "7h",
    "8a",
    "8b",
    "8c",
    "8d",
    "8e",
    "8f",
    "8g",
    "8h",
]


def is_Valid_Chess_Board(dic):
    black_pieces = {}
    white_pieces = {}

    for key, value in dic.items():  # seperate the pieces in white/black
        if value[0] == "b":
            black_pieces[key] = value
        elif value[0] == "w":
            white_pieces[key] = value

    only_piece_name_black = list(black_pieces.values())
    only_piece_name_white = list(white_pieces.values())

    if (
        (len(black_pieces) <= 16 and len(white_pieces) <= 16)
        and (
            only_piece_name_black.count("bking") == 1
            and only_piece_name_white.count("wking") == 1
        )
        and (
            only_piece_name_black.count("bpawn") <= 8
            and only_piece_name_white.count("wpawn") <= 8
        )
    ):
        check_one = True
    else:
        check_one = False

    check_two = all(item in valid_board for item in dic.keys())

    return check_one and check_two


print(is_Valid_Chess_Board(example_board))
