"""
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without importing it. 
This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to
9 × 9. You’ll need to implement the following features:
•	 If the user enters the correct answer, the program displays “Correct!”
for 1 second and moves on to the next question.
•	 The user gets three tries to enter the correct answer before the
program moves on to the next question.
•	 Eight seconds after first displaying the question, the question is
marked as incorrect even if the user enters the correct answer after
the 8-second limit.
Compare your code to the code using PyInputPlus in “Project:
Multiplication Quiz” on page 196.
"""

import random, time

number_of_questions = 3
correct_answers = 0
amount_of_chance = 3
time_limit = 8

for question_number in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    for chance in range(amount_of_chance + 1):  # +1 only to print 'Out of tries'
        if chance == amount_of_chance:
            print("Out of tries")
            break
        given_answer = int(input(f"#{question_number+1}: {num1} x {num2} \n"))
        time_check = time.time()  # starts the timer
        if time.time() >= time_check + time_limit:  
            print("Out of time")
            break
        if given_answer == (num1 * num2):
            correct_answers += 1
            print("Correct")
            break
        else:
            print("Incorrect")
    time.sleep(1)
print(f'Score: {correct_answers}/{number_of_questions}')
