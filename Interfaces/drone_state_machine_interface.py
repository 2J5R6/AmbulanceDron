import tkinter as tk
from transitions import Machine
from tkinter import messagebox

class DroneStateMachine:
    states = ['waiting', 'navigating', 'arrived', 'returning', 'completed', 'low_battery', 'obstacle_detected', 'gps_lost', 'high_turbulence', 'engine_failure', 'landing_spot_free', 'landing_spot_occupied', 'vital_signs_detected', 'electric_shock_commanded']

    def __init__(self):
        self.machine = Machine(model=self, states=DroneStateMachine.states, initial='waiting')
        self.machine.add_transition('start_navigation', 'waiting', 'navigating')
        self.machine.add_transition('arrive', 'navigating', 'arrived')
        self.machine.add_transition('return', 'arrived', 'returning')
        self.machine.add_transition('complete', 'returning', 'completed')
        self.machine.add_transition('battery_low', '*', 'low_battery')
        self.machine.add_transition('obstacle_fixed', '*', 'obstacle_detected')
        self.machine.add_transition('obstacle_moving', '*', 'obstacle_detected')
        self.machine.add_transition('gps_signal_lost', '*', 'gps_lost')
        self.machine.add_transition('turbulence_detected', '*', 'high_turbulence')
        self.machine.add_transition('engine_fail', '*', 'engine_failure')
        self.machine.add_transition('landing_spot_found', '*', 'landing_spot_free')
        self.machine.add_transition('landing_spot_occupied', '*', 'landing_spot_occupied')
        self.machine.add_transition('detect_vital_signs', '*', 'vital_signs_detected')
        self.machine.add_transition('command_electric_shock', '*', 'electric_shock_commanded')

    def run_interface(self):
        window = tk.Tk()
        window.title("Drone State Machine Interface")

        state_label = tk.Label(window, text="Estado actual del dron: " + self.state)
        state_label.pack()

        def update_state():
            state_label.config(text="Estado actual del dron: " + self.state)

        # Botones para cada transición
        tk.Button(window, text="Start Navigation", command=lambda: [self.start_navigation(), update_state(), messagebox.showinfo("Estado del Dron", "Navegación iniciada")]).pack()
        tk.Button(window, text="Arrive", command=lambda: [self.arrive(), update_state(), messagebox.showinfo("Estado del Dron", "Dron ha llegado")]).pack()
        tk.Button(window, text="Return", command=lambda: [self.return(), update_state(), messagebox.showinfo("Estado del Dron", "Retornando")]).pack()
        tk.Button(window, text="Complete Mission", command=lambda: [self.complete(), update_state(), messagebox.showinfo("Estado del Dron", "Misión completada")]).pack()
        tk.Button(window, text="Battery Low", command=lambda: [self.battery_low(), update_state(), messagebox.showinfo("Alerta del Dron", "Batería baja")]).pack()
        tk.Button(window, text="Obstacle Detected (Fixed)", command=lambda: [self.obstacle_fixed(), update_state(), messagebox.showinfo("Alerta del Dron", "Obstáculo fijo detectado")]).pack()
        tk.Button(window, text="Obstacle Detected (Moving)", command=lambda: [self.obstacle_moving(), update_state(), messagebox.showinfo("Alerta del Dron", "Obstáculo móvil detectado")]).pack()
        tk.Button(window, text="GPS Signal Lost", command=lambda: [self.gps_signal_lost(), update_state(), messagebox.showinfo("Alerta del Dron", "Señal de GPS perdida")]).pack()
        tk.Button(window, text="High Turbulence Detected", command=lambda: [self.turbulence_detected(), update_state(), messagebox.showinfo("Alerta del Dron", "Alta turbulencia detectada")]).pack()
        tk.Button(window, text="Engine Failure", command=lambda: [self.engine_fail(), update_state(), messagebox.showinfo("Alerta del Dron", "Falla en el motor")]).pack()
        tk.Button(window, text="Landing Spot Free", command=lambda: [self.landing_spot_found(), update_state(), messagebox.showinfo("Estado del Dron", "Lugar de aterrizaje libre")]).pack()
        tk.Button(window, text="Landing Spot Occupied", command=lambda: [self.landing_spot_occupied(), update_state(), messagebox.showinfo("Alerta del Dron", "Lugar de aterrizaje ocupado")]).pack()
        tk.Button(window, text="Vital Signs Detected", command=lambda: [self.detect_vital_signs(), update_state(), messagebox.showinfo("Estado del Dron", "Signos vitales detectados")]).pack()
        tk.Button(window, text="Command Electric Shock", command=lambda: [self.command_electric_shock(), update_state(), messagebox.showinfo("Acción del Dron", "Descarga eléctrica comandada")]).pack()

        window.mainloop()

# Crear una instancia de DroneStateMachine y ejecutar la interfaz
drone_state_machine = DroneStateMachine()
drone_state_machine.run_interface()
