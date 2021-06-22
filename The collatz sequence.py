""""
Write a function named collatz() that has one parameter named number. If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that
keeps calling collatz() on that number until the function returns the value 1
"""


def collatz(num): 
    if num % 2:  # odd
        num10 = 3 * num + 1
    else:  # even
        num10 = num // 2

    if num10 != 1:
        print(num10)
        collatz(num10)
    else:
        print(num10)

def give_me_a_number():
    num = input("Give me a number:\n")
    try:
        num = int(num)
        collatz(num)
    except ValueError:
        print('Please enter an integer!')

give_me_a_number()
