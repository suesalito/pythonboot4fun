class Human(object):

    def __init__(self,budget):
        self.budget = budget

    def addbudget(self,money):
        self.budget += money

    pass

tonk = Human(1000)
print (tonk.budget)
tonk.addbudget(200)
print (tonk.budget)

class Deck(object):

    card = set()
    card = []


