#create a class Car that can be used to instatiate various objects
class Car(object):
    name='General'
    model='GM'
    num_of_doors=4
    speed=0


    def __init__( self, name='General', model='GM', car_type='car', num_of_wheels=4, num_of_doors=4):
        self.name=name
        self.model=model
        self.car_type=car_type
        self.speed=0
        num_of_wheels=4


        #number of doors
        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        # Number of Wheels
        if (self.car_type == 'trailer'):
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4


    # is_saloon Car
    def is_saloon(self):
        if self.car_type != 'trailer':
            return True
        else:
            return False


    # Car Speed
    def drive(self, accelerate):
        if (self.car_type == 'trailer'):
            self.speed = int(accelerate * 11)
            return self
        else:
            if(accelerate !=0):
                self.speed = 10 ** accelerate
            else:
                self.speed = 10 * accelerate
            return self
