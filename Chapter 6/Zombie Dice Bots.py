import zombiedice
import random

# A bot that, after the first roll, randomly decides if it will continue or stop
def random_roll():
    random_pick = random.choice([True, False])
    if random_pick:
        zombiedice.roll()
    else:
        pass


# A bot that stops rolling after it has rolled two brains
def two_brain_roll(diceRollResults):
    brains = 0
    while diceRollResults is not None:
        brains += diceRollResults["brains"]

        if brains < 2:
            diceRollResults = zombiedice.roll()  # roll again
        else:
            break


# A bot that stops rolling after it has rolled two shotguns
def two_shotgun_roll(diceRollResults):
    shotgun = 0
    while diceRollResults is not None:
        shotgun += diceRollResults["shotgun"]
        if shotgun < 2:
            diceRollResults = zombiedice.roll()
        else:
            break


# A bot that initially decides it’ll roll the dice one to four times, but will
# stop early if it rolls two shotguns
def random_roll_bot(diceRollResults):
    shotgun = 0
    random_roll = random.randint(1, 4)
    for x in range(random_roll):
        if diceRollResults is not None:
            shotgun += diceRollResults["shotgun"]
        if shotgun == 2:
            break
        else:
            diceRollResults = zombiedice.roll()


# A bot that stops rolling after it has rolled more shotguns than brains
def more_guns_than_brains(diceRollResults):
    shotgun = 0
    brains = 0
    while diceRollResults is not None:
        shotgun += diceRollResults["shotgun"]
        brains += diceRollResults["brains"]
        if shotgun > brains:
            break
        else:
            diceRollResults = zombiedice.roll()


# Al Sweigert code start here
class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        # call here one of the bots here
        random_roll_bot(diceRollResults)


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name="Random"),
    zombiedice.examples.RollsUntilInTheLeadZombie(name="Until Leading"),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name="Until 2 Shotguns", minShotguns=2
    ),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name="Until 1 Shotgun", minShotguns=1
    ),
    MyZombie(name="My Zombie Bot"),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
