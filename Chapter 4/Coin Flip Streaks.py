"""
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a
rnadomly generated list of heads and tails. Your program breaks up the experiment into two parts:
the first generates a list of randomly selected 'heads' and 'tails values, and the second part 
check if there is a streak in it. Put all of this code in a loop that repeats the experiment 10.000
times so we can find out what percentage of the coin flips contains a streak of six heads or tails in 
a row.
"""

import random

experiments = 10000
number_of_toss = 100
number_of_streaks = 0
same_consecutive_toss = 5

for x in range(experiments):
    head_or_tails = [random.choice(["H", "T"]) for _ in range(number_of_toss)]
    streak = 0
    for x, y in zip(head_or_tails, head_or_tails[1:]):
        if x == y:
            streak += 1
            if streak == same_consecutive_toss:
                number_of_streaks += 1
                break
        else:
            streak = 0

print("Chance of streak: %s%%" % (number_of_streaks / 100))
