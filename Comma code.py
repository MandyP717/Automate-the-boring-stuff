"""
Write a function that takes a list value as an argument and returns a string with all
the items seperated by a comma and a space, with and inserted before the last item.
"""


def comma_code(join_list):
    if len(join_list) > 2:
        convert_list = [str(item) for item in join_list]
        joined_string = ", ".join(convert_list[:-1])
        return f"{joined_string} and {convert_list[-1]}"
    elif len(join_list) == 2:
        return f"{join_list[0]} and {join_list[1]}"
    else:
        return join_list


spam = ["apples", "bananas", "tofu", "cats"]
spam2 = []
spam3 = ["apples", "bananas"]
spam4 = ["apples", 3, "bananas", 4, "!"]
spam5 = ['apples']

print(comma_code(spam))
print(comma_code(spam2))
print(comma_code(spam3))
print(comma_code(spam4))
print(comma_code(spam5))