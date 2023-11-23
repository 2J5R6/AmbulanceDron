# actors.py

class Drone:
    def __init__(self, identifier, propellers, max_payload, battery_level=100):
        self.identifier = identifier
        self.propellers = propellers
        self.max_payload = max_payload
        self.battery_level = battery_level
        self.current_location = (0, 0)  # Asignación de una ubicación inicial por defecto
        self.destination = (0, 0)
        self.is_operational = True

    def navigate_to(self, location):
        if self.battery_level > 20:  # Asegurarse de que hay suficiente batería
            self.destination = location
            print(f"Drone {self.identifier} is navigating to {location}.")
        else:
            print("Not enough battery to navigate.")

    def update_battery_level(self, level):
        self.battery_level = level
        if level < 20:
            print("Warning: Low battery. Please charge soon.")

    def perform_diagnostics(self):
        print(f"Performing diagnostics on drone {self.identifier}.")

class Person:
    def __init__(self, name, identification, location):
        self.name = name
        self.identification = identification
        self.location = location

class User(Person):
    def __init__(self, name, identification, location):
        super().__init__(name, identification, location)

    def report_emergency(self, location):
        print(f"{self.name} is reporting an emergency at {location}.")

class Beneficiary(Person):
    def __init__(self, name, identification, location, medical_condition):
        super().__init__(name, identification, location)
        self.medical_condition = medical_condition

class TheCenter:
    def __init__(self):
        self.drones = {}
        self.operators = []

    def add_drone(self, drone):
        self.drones[drone.identifier] = drone

    def dispatch_drone(self, drone_identifier, location):
        if drone_identifier in self.drones:
            drone = self.drones[drone_identifier]
            if drone.is_operational:
                drone.navigate_to(location)
                print(f"Drone {drone.identifier} has been dispatched to {location}.")
            else:
                print(f"Drone {drone.identifier} is not operational.")
        else:
            print(f"No drone with identifier {drone_identifier} found.")
