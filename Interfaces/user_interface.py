import tkinter as tk
from tkinter import messagebox
from Interfaces.the_center_interface import start_center_interface

def report_emergency(name, location, emergency_type, beneficiary_name, emergency_data, the_center, drone_state_machine):
    emergency_data['name'] = name
    emergency_data['location'] = location
    emergency_data['emergency_type'] = emergency_type
    emergency_data['beneficiary_name'] = beneficiary_name
    messagebox.showinfo("Emergencia Reportada", "Tu reporte de emergencia ha sido enviado.")
    start_center_interface(the_center, drone_state_machine, emergency_data)

def start_user_interface(emergency_data, the_center, drone_state_machine):
    window = tk.Tk()
    window.title('User Emergency Interface')

    # Campos de entrada
    tk.Label(window, text="Nombre:").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="Ubicación (coordenadas):").pack()
    location_entry = tk.Entry(window)
    location_entry.pack()

    tk.Label(window, text="Tipo de Emergencia:").pack()
    emergency_type_entry = tk.Entry(window)
    emergency_type_entry.pack()

    tk.Label(window, text="Nombre del Beneficiario:").pack()
    beneficiary_name_entry = tk.Entry(window)
    beneficiary_name_entry.pack()

    # Botón para reportar emergencia
    report_button = tk.Button(window, text="Reportar Emergencia", 
                              command=lambda: report_emergency(
                                  name_entry.get(), 
                                  location_entry.get(), 
                                  emergency_type_entry.get(), 
                                  beneficiary_name_entry.get(),
                                  emergency_data, the_center, drone_state_machine))
    report_button.pack()

    window.mainloop()
