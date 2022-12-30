from abc import ABC, abstractmethod
import csv
from pprint import pprint



class Cupcake(ABC):

    size = 'regular'

    def __init__(self, name, price, flavor, frosting, filling):
        
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
    
    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

# my_cupcake = Cupcake('Unicorn', 3.99, 'strawberry', 'vanilla', 'strawberry cream')
# my_cupcake.frosting = 'pink'
# my_cupcake.filling = 'lemon'
# my_cupcake.name = 'Pink Lemonade'

# # my_cupcake.is_miniature = False
# # print(my_cupcake.is_miniature)

# my_cupcake.add_sprinkles('rainbow')
# print(my_cupcake.sprinkles)

class Mini(Cupcake):
    size = 'mini'

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
    
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)


class Regular(Cupcake):
    size = 'regular'

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)

class Giant(Cupcake):
    size = 'giant'

    def calculate_price(self, quantity):
        return super().calculate_price(quantity)


def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)
# read_csv('sample.csv')

my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")
my_cupcake_mini.add_sprinkles('chocolate')
my_cupcake_regular = Regular('Unicorn', 3.99, 'vanilla', 'chocolate', 'strawberry')
my_cupcake_regular.add_sprinkles('rainbow')
my_cupcake_giant = Giant('Peach Cobbler', 9.99, 'peach', 'vanilla', 'peach')
my_cupcake_giant.add_sprinkles('cinnamon sugar')
choco_cake = Regular('Death by Chocolate', 3.99, 'Chocolate', 'chocolate', 'chocolate')
choco_cake.add_sprinkles('chocolate')

cupcake_list = [my_cupcake_mini, my_cupcake_regular, my_cupcake_giant, choco_cake]




def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

# write_new_csv('sample.csv', cupcake_list)
# write_new_csv('cupcakes.csv', cupcake_list)
# write_new_csv('orders.csv', choco_cake)

def add_cupcake(file, cupcake):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, 'filling'):
            writer.writerow({'size': cupcake.size, 'name': cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

new_cupcake = Regular('Lemon Blueberry', 4.99, 'lemon', 'buttercream', 'blueberry jam')

# add_cupcake('cupcakes.csv', new_cupcake)

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake['name'] == name:
            return cupcake
    return None

def add_cupcake_dict(file, cupcake):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)