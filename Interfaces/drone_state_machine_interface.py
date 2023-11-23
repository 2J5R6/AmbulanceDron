from transitions import Machine

class DroneStateMachine:
    states = ['idle', 'navigating', 'monitoring', 'manual_control', 'landing', 'emergency_handling']

    def __init__(self):
        # Inicializar la máquina de estados
        self.machine = Machine(model=self, states=DroneStateMachine.states, initial='idle')

        # Añadir transiciones
        self.machine.add_transition(trigger='low_battery', source='*', dest='idle')
        self.machine.add_transition(trigger='obstacle_detected', source='navigating', dest='manual_control')
        self.machine.add_transition(trigger='gps_lost', source='navigating', dest='manual_control')
        self.machine.add_transition(trigger='high_turbulence', source='*', dest='manual_control')
        self.machine.add_transition(trigger='engine_failure', source='*', dest='emergency_handling')
        self.machine.add_transition(trigger='landing_site_clear', source='*', dest='landing')
        self.machine.add_transition(trigger='landing_site_occupied', source='landing', dest='manual_control')
        self.machine.add_transition(trigger='flight_start_command', source='idle', dest='navigating')
        self.machine.add_transition(trigger='emergency_location_received', source='*', dest='navigating')
        self.machine.add_transition(trigger='emergency_location_updated', source='navigating', dest='navigating')
        self.machine.add_transition(trigger='vital_signs_detected', source='*', dest='emergency_handling')
        self.machine.add_transition(trigger='electrical_discharge_command', source='emergency_handling', dest='emergency_handling')

        # Definir acciones para entrar y salir de cada estado
        self.machine.on_enter_idle('enter_idle')
        self.machine.on_enter_navigating('enter_navigating')
        self.machine.on_enter_monitoring('enter_monitoring')
        self.machine.on_enter_manual_control('enter_manual_control')
        self.machine.on_enter_landing('enter_landing')
        self.machine.on_enter_emergency_handling('enter_emergency_handling')

    # Métodos on_enter para cada estado
    def enter_idle(self):
        print("Drone is now idle due to low battery or completion of tasks.")

    def enter_navigating(self):
        print("Drone is navigating to the destination.")

    def enter_monitoring(self):
        print("Drone is monitoring the situation.")

    def enter_manual_control(self):
        print("Drone is under manual control due to obstacles or other issues.")

    def enter_landing(self):
        print("Drone is landing.")

    def enter_emergency_handling(self):
        print("Drone is handling an emergency situation.")
