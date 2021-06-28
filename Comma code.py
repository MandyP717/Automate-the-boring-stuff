"""
Write a function that takes a list value as an argument and returns a string with all
the items sperated by a comma and a space, with and inserted before the last item.
"""


def comma_code(join_list):
    try:
        join_list[-1] = f'and {join_list[-1]}'
        comma =  ", ".join(join_list)
    except:
        comma = join_list
    return comma

spam = ["apples", "bananas", "tofu", "cats"]
spam2 = []
print(comma_code(spam))
print(comma_code(spam2))
