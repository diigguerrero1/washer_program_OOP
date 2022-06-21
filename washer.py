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

    def wash(self):
        self._fill_water_tank()
        self._add_soap()
        self._wash()
        self._spin_dry()

    def _fill_water_tank(self):

        if self.water_level == 1:
            water_level = 'bajo'
        elif self.water_level == 2:
            water_level = 'medio'
        elif self.water_level == 3:
            water_level = 'alto'

        print(f'Se esta llenando en tanque con nivel: {water_level}')

    def _add_soap(self):
        print(f'Se esta agregando el jabón')

    def _wash(self):
        print(f'Se esta lavando')

    def _spin_dry(self):
        print(f'Se esta centrifugando')



    

