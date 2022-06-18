# Module of the operating system
import os

# Module of configuration of Project
from config import config

# Module of Classes of the Project
from washer import Washer, Washer_Motor


# Vars of configuration of project
washer_type_dict = config()['washer']['washer_type']
water_level_dict = config()['washer']['water_level']
dirt_level_dict = config()['washer']['dirt_level']
aditional_functions_dict = config()['washer']['aditional_functions']
power = config()['washer']['Motor']['power']


# Function for activate washer motor and all wash
def initialition_washer(status, washer_type, water_level, dirt_level, aditional_functions):

    # Se necesita definir a traves de condicionales el tipo de power que necesita el motor dependiendo las especificaciones del cliente.

    if water_level == 1:
        power_motor = power['low_power']
    elif water_level == 2:
        power_motor = power['medium_power']
    elif water_level == 3:
        power_motor = power['high_power']

    washer = Washer(status, washer_type, water_level, dirt_level, aditional_functions, Washer_Motor(status, "k37973hj0", power_motor))

    print(vars(washer))
    print(vars(washer._motor))


# Function what define the methoth of wash, and the vars for activate the washer motor
def start_washer():

    status = False

    start = input("desea arrancar la lavadora y/n: ")

    if start == "y":

        status = True

        print("Lave si tiene la suficiente ropa sucia. Seleccione las caracteristicas de su lavado")

        print(f'Tipos de lavado: {washer_type_dict}')
        washer_type = int(input("escoja el tipo de lavado con el respectivo número: "))

        print(f'Niveles de agua: {water_level_dict}')
        water_level = int(input("Escoge el nivel de agua con el respectivo número: "))

        print(f'Nivel de suciedad: {dirt_level_dict}')
        dirt_level = int(input("Escoja el nivel de suciedad con el respectivo número: "))

        print(f'Funciones adicionales: {aditional_functions_dict}')
        aditional_functions = int(input("Escoja las funciones adicionales con el respectivo número: "))

    elif start == "n":
        print("Gracias por no usar agua innecesariamente")
    else:
        print("No elegiste ninguna opción correcta, vuelve a intentarlo nuevamente.")

    return status, washer_type, water_level, dirt_level, aditional_functions

# Function for runing the program
def run():
    status, washer_type, water_level, dirt_level, aditional_functions = start_washer()
    initialition_washer(status, washer_type, water_level, dirt_level, aditional_functions)


if __name__ == "__main__":
    os.system("cls")
    run()

