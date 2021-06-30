alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a_number = [1, 2, 3, 4, 5, 6, 7, 8]

valid_board = []

for x in alpabet:
    for y in a_number:
        valid_board.append(x + str(y))

valid_board2 = [x + str(y) for x in alpabet for y in a_number]
print(valid_board)
print(valid_board2)
