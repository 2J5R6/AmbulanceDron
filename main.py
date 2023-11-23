from Models.actors import Drone, User, Beneficiary, TheCenter
from Interfaces.drone_state_machine_interface import DroneStateMachine
from Interfaces.user_interface import start_user_interface
from Interfaces.the_center_interface import start_center_interface

def main():
    # Crear instancias de los actores
    drone = Drone(identifier="Drone1", propellers=4, max_payload=5)
    user = User(name="User1", identification="ID123", location=(0, 0))
    beneficiary = Beneficiary(name="Ben1", identification="ID456", location=(0, 0), medical_condition="Condition")
    the_center = TheCenter()

    # Asegúrate de que 'drones' en TheCenter es una lista
    if not hasattr(the_center, 'drones') or not isinstance(the_center.drones, list):
        the_center.drones = []
    
    the_center.drones.append(drone)
    
    # Crear la máquina de estados del dron
    drone_state_machine = DroneStateMachine()
    
    # Iniciar interfaces de usuario y centro de control
    emergency_data = {}  # Diccionario para almacenar datos de emergencia
    start_user_interface(emergency_data)
    start_center_interface(the_center, drone_state_machine, emergency_data)

if __name__ == "__main__":
    main()
