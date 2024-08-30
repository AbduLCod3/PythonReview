class Vehicle :
     # Propertie
    def __init__(self, make, model):
        self.make = make
        self.model = model

    #Methods
    def moves(self):
        print('Moves a long..')

    def get_make_model(self):
        print(f'I am {self.make} {self.model}')

# an object
my_car = Vehicle('Tesla', 'Model 3')
your_car = Vehicle('Cadillac', 'Escalade')


# print(my_car.make)
# print(my_car.model)

# Use the getter function to get the attributes
my_car.get_make_model()
my_car.moves()

your_car.get_make_model()
your_car.moves()

# Inheritance 

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        ## to inherit everying from the top 
        #self.make = make
        ##self.model = model
        ## Use the super method instead
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies a long..')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles a long..')


class GolfCart(Vehicle):
    pass


# Objects

cessna = Airplane("Cessna", 'Skyhawk', 'N-12345')
mack = Truck("Mack", 'Pinnacle')
golfwagon = GolfCart("Yamaha", 'GC100')


# Calling Methods
# cessna.get_make_model()
# cessna.moves()
# mack.get_make_model()
# mack.moves()
# golfwagon.get_make_model()
# golfwagon.moves()

print('\n\n')

# Polymorphism - The ability to behave differently in response to the same input messages
for v in (my_car, your_car, cessna, mack, golfwagon):
    # Here we are calling the same methods
    # but will behave differently based on how the above classes was built
    v.get_make_model()
    v.moves()
