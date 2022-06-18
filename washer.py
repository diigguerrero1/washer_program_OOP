# Class what define the Motor of Washer
class Washer_Motor:

    stauts = bool
    reference = str
    power = str

    def __init__(self, status, reference, power):
        self.status = status
        self.reference = reference
        self.power = power

    def start(self):
        if self.stauts == True:
            pass


# Class what define the washer and their methoths
class Washer:

    status = bool
    washer_type = int
    water_level = int
    dirt_level = int
    aditional_functions = int
    motor = Washer_Motor("", "", "")

    def __init__(self, status, washer_type, water_level, dirt_level, aditional_functions, motor):
        self.stauts = status
        self.washer_type = washer_type
        self.water_level = water_level
        self.dirt_level = dirt_level
        self.aditional_functions = aditional_functions
        self._motor = motor

    def encender(self):
        if self.stauts == True:
            motor = self._motor
        else:
            motor = False


    

