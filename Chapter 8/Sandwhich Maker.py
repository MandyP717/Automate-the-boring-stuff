"""
Sandwich Maker
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:
•	 Using inputMenu() for a bread type: wheat, white, or sourdough.
•	 Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
•	 Using inputYesNo() to ask if they want cheese.
•	 If so, using inputMenu() to ask for a cheese type: cheddar, Swiss,
or mozzarella.
•	 Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
•	 Using inputInt() to ask how many sandwiches they want. Make sure this
number is 1 or more.
Come up with prices for each of these options, and have your program
display a total cost after the user enters their selection.
"""

import pyinputplus as pyip


def which_bread():
    bread_prices = {"wheat": 0.8, "white": 0.75, "sourdough": 0.9}
    bread_choice = pyip.inputMenu(["wheat", "white", "sourdough"], numbered=True)
    return bread_choice, bread_prices.get(bread_choice)


def which_protein():
    protein_prices = {"chicken": 1.2, "turkey": 1.3, "ham": 1.2, "tofu": 1.0}
    protein_choice = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], numbered=True)
    return protein_choice, protein_prices.get(protein_choice)


def which_cheese():
    cheese_prices = {"cheddar": 0.5, "Swiss": 0.75, "mozzarella": 0.80}
    answer = pyip.inputYesNo("Do you want cheese, y/n? ")
    if answer == "yes":
        cheese = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], numbered=True)
        return cheese, cheese_prices.get(cheese)
    else:
        return "no", 0.0


def extras():
    condiments_prices = {"mayo": 0.4, "mustard": 0.45, "lettuce": 0.6, "tomato": 0.65}
    condiments = ["mayo", "mustard", "lettuce", "tomato"]
    client_picks = [
        extra
        for extra in condiments
        if pyip.inputYesNo(f"Do you want {extra}, y/n? ") == "yes"
    ]
    total_price = sum([condiments_prices.get(item) for item in client_picks])

    # convert list to a string
    if len(client_picks) > 2:
        client_picks.insert(-1, "and")
        condiments_string = (
            ", ".join(client_picks[:-2]) + " " + " ".join(client_picks[-2:])
        )
    if len(client_picks) == 2:
        client_picks.insert(-1, "and")
        condiments_string = " ".join(client_picks)
    if len(client_picks) == 1:
        condiments_string = client_picks[0]
    if len(client_picks) < 1:
        condiments_string = "no condiments"
    return condiments_string, total_price


bread, bread_total = which_bread()
protein, protein_total = which_protein()
cheese, cheese_total = which_cheese()
condiments, condiments_total = extras()

print("\n")
print(
    f"Your sandwhich consist of {bread} bread filled with {protein} and {cheese} cheese dressed with {condiments}."
)
amount_sandwhiches = pyip.inputInt("How many of this sandwhich do you want? ", min=1)
print(
    "Your total is",
    str(
        sum([bread_total, protein_total, cheese_total, condiments_total])
        * amount_sandwhiches
    )
    + ".",
)
