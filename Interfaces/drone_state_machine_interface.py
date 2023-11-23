import tkinter as tk
from tkinter import messagebox
from transitions import Machine

class DroneStateMachine:
    states = ['en tierra', 'navegando', 'detectando obstáculos', 'batería baja', 'en emergencia']

    def __init__(self):
        self.machine = Machine(model=self, states=DroneStateMachine.states, initial='en tierra')
        self.machine.add_transition('iniciar_vuelo', 'en tierra', 'navegando')
        self.machine.add_transition('detectar_obstáculo', 'navegando', 'detectando obstáculos')
        self.machine.add_transition('batería_baja', '*', 'batería baja')
        self.machine.add_transition('emergencia', '*', 'en emergencia')
        self.machine.add_transition('aterrizar', '*', 'en tierra')

class DroneInterface:
    def __init__(self, master, drone_state_machine):
        self.master = master
        self.drone_state_machine = drone_state_machine
        self.master.title("Simulación de Dron")

        self.state_label = tk.Label(master, text="Estado actual: en tierra")
        self.state_label.pack()

        self.iniciar_vuelo_button = tk.Button(master, text="Iniciar Vuelo", command=self.iniciar_vuelo)
        self.iniciar_vuelo_button.pack()

        # Agrega aquí más botones para otros eventos

    def update_state_label(self):
        self.state_label.config(text=f"Estado actual: {self.drone_state_machine.state}")

    def iniciar_vuelo(self):
        self.drone_state_machine.iniciar_vuelo()
        messagebox.showinfo("Cambio de Estado", "El dron ha iniciado vuelo")
        self.update_state_label()
        # Actualiza la interfaz según el nuevo estado

        # Agrega aquí más métodos para manejar otros eventos

# Creación de la ventana principal y la máquina de estados
root = tk.Tk()
drone_sm = DroneStateMachine()
app = DroneInterface(root, drone_sm)

root.mainloop()
