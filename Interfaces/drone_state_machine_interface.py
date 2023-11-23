import tkinter as tk
from transitions import Machine

class DroneStateMachine:
    states = ['waiting', 'navigating', 'arrived', 'returning', 'completed']

    def __init__(self):
        self.machine = Machine(model=self, states=DroneStateMachine.states, initial='waiting')
        self.machine.add_transition(trigger='dispatch', source='waiting', dest='navigating')
        self.machine.add_transition(trigger='arrive', source='navigating', dest='arrived')
        self.machine.add_transition(trigger='return', source='arrived', dest='returning')
        self.machine.add_transition(trigger='complete', source='returning', dest='completed')

    def run_interface(self):
        window = tk.Tk()
        window.title("Drone State Machine Interface")

        state_label = tk.Label(window, text="Estado actual del dron: " + self.state)
        state_label.pack()

        def update_state():
            state_label.config(text="Estado actual del dron: " + self.state)

        tk.Button(window, text="Dispatch", command=lambda: [self.dispatch(), update_state()]).pack()
        tk.Button(window, text="Arrive", command=lambda: [self.arrive(), update_state()]).pack()
        tk.Button(window, text="Return", command=lambda: [self.return_(), update_state()]).pack()
        tk.Button(window, text="Complete", command=lambda: [self.complete(), update_state()]).pack()

        window.mainloop()

