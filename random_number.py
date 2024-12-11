import random

# for i in range(3):
#     print(random.randint(10, 20))

# members = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader)

class Dice:
    @staticmethod
    def roll():
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return  first, second #automatically return this as a tuple, we don't need parenthesis ()

dice = Dice()
print(dice.roll())