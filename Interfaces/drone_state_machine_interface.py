from transitions import Machine
import tkinter as tk
from tkinter import messagebox

class DroneStateMachine(object):
    states = ['idle', 'navigating', 'obstacle_detected', 'low_battery', 'emergency_location_changed', 'landing', 'dealing_with_emergency']

    def __init__(self):
        self.machine = Machine(model=self, states=DroneStateMachine.states, initial='idle')

        # Definir transiciones
        self.machine.add_transition('start_flight', 'idle', 'navigating')
        self.machine.add_transition('detect_obstacle', 'navigating', 'obstacle_detected')
        self.machine.add_transition('low_battery_alert', '*', 'low_battery')
        self.machine.add_transition('change_emergency_location', '*', 'emergency_location_changed')
        self.machine.add_transition('land', ['navigating', 'obstacle_detected', 'low_battery', 'emergency_location_changed'], 'landing')
        self.machine.add_transition('deal_with_emergency', 'landing', 'dealing_with_emergency')
        self.machine.add_transition('reset', '*', 'idle')

        # Agregar callbacks para entrar y salir de estados
        self.on_enter_idle = self.on_enter_idle_callback
        self.on_enter_navigating = self.on_enter_navigating_callback
        # Agrega aquí más callbacks según sea necesario

    def on_enter_idle_callback(self):
        print("Drone is now idle.")

    def on_enter_navigating_callback(self):
        print("Drone is now navigating.")

    # Agrega aquí más métodos de callback según sea necesario

# Crear la interfaz de usuario
class DroneInterface:
    def __init__(self, master, drone_state_machine):
        self.master = master
        self.drone_state_machine = drone_state_machine
        master.title("Drone State Machine Simulation")

        # Botones para controlar el dron
        self.start_flight_button = tk.Button(master, text="Start Flight", command=self.start_flight)
        self.start_flight_button.pack()

        self.detect_obstacle_button = tk.Button(master, text="Detect Obstacle", command=self.detect_obstacle, state=tk.DISABLED)
        self.detect_obstacle_button.pack()

        # Agrega aquí más botones para otros eventos

    def update_buttons(self):
        # Actualizar el estado de los botones según el estado del dron
        if self.drone_state_machine.state == 'navigating':
            self.detect_obstacle_button['state'] = tk.NORMAL
        else:
            self.detect_obstacle_button['state'] = tk.DISABLED

        # Agrega aquí más lógica para otros botones

    def start_flight(self):
        self.drone_state_machine.start_flight()
        messagebox.showinfo("Drone Status", "Flight Started")
        self.update_buttons()

    def detect_obstacle(self):
        self.drone_state_machine.detect_obstacle()
        messagebox.showinfo("Drone Status", "Obstacle Detected")
        self.update_buttons()

    # Agrega aquí más métodos para manejar eventos de botones

# Ejecutar la interfaz
root = tk.Tk()
drone_sm = DroneStateMachine()
app = DroneInterface(root, drone_sm)
root.mainloop()
