"""Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters, 
and has at least one digit. You may need to test the string against multiple 
regex patterns to validate its strength."""

import re

# test password
strong_password = "9sP7RKvmTuBJgmTLvLy"
short_password = "PAu2Mr"
no_digit_password = "LXqGnShmFFfRGvBt"
no_lowercase_password = "G'X&'4$8'D<2(MZ;"
no_uppercase_password = "4z`xubr+p,qe7(ym"

""" 
(?=(.*RULE){MIN_OCCURANCES,})
^ - start of string
$ - end of string
(?=...) - positive look ahead
* - control verb
{} - {min. occ., max. occ}
. - any character
\d - any digit
[a-z] - lowercase
[A-Z] - uppercase
"""


def check_for_strong_password(password):
    regex = re.compile(r"^(?=(.*[a-z]{1,}))(?=(.*\d){1,})(?=(.*[A-Z]){1,}).{8,}$")
    if re.match(regex, password):
        print("It is a strong password")
    else:
        print("It is a weak password")


check_for_strong_password(strong_password)
