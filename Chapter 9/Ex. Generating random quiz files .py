import random

# The quiz data. Keys are states and values are their capitals.
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}
# Generate 35 quiz files.

for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open(f"capitalsquiz{quizNum + 1}.txt", "w")  # Create file of random quiz
    answerKeyFile = open(
        f"capitalsquiz_answers{quizNum + 1}.txt", "w"
    )  # Create the answer file

    # Write out the header for the quiz.
    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")                                 # Write header of random quiz
    quizFile.write((" " * 20) + f"State Capitals Quiz (Form{quizNum + 1})")         #Tab in "string"
    quizFile.write("\n\n")                                                              

    # Shuffle the order of the states.
    states = list(capitals.keys())                                                  
    random.shuffle(states)                                                          #shuffle the states around

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):                                               
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]                               #Correct answer of first question in the shuffled list states       
        wrongAnswers = list(capitals.values())                                      #Create list of all values in capital
        del wrongAnswers[wrongAnswers.index(correctAnswer)]                         #Del the correct answer from the list
        wrongAnswers = random.sample(wrongAnswers, 3)                               #Choose 3 random capital(values) from the list
        answerOptions = wrongAnswers + [correctAnswer]                              #Create a new list with 1 correct answer and 3 random wrong answer
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write(
            f"{questionNum + 1}. What is the capital of {states[questionNum]}?\n"   #Write The question to the file
        )
        for i in range(4):
            quizFile.write(f" {'ABCD'[i]}. {answerOptions[i]}\n")                   #Create the A. B. C. D. Answer to the file
        quizFile.write("\n")
        # Write the answer key to a file.
        answerKeyFile.write(
            f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}"       #Write correct answer to the answer file.
        )
    quizFile.close()
    answerKeyFile.close()
