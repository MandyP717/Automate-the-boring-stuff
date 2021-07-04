"""Write a function named print_table() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified. 
Assume that all the inner lists will contain the same number of strings."""

table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def length_inner_list(table):
    max_length = [max([len(item) for item in inner_list]) for inner_list in table_data]
    return max_length

def rjust_table(table):
    transpose_list = [list(i) for i in zip(*table_data)]
    for row in transpose_list:
        print (' '.join(item.rjust(width) for item, width in zip(row, length_inner_list(table))))


rjust_table(table_data)