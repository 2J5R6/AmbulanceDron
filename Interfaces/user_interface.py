import tkinter as tk
from tkinter import messagebox

def report_emergency(name, location, emergency_type, beneficiary_name):
    # Aquí se enviarían los datos al centro de control
    print(f"Emergencia reportada por {name} en {location}. Tipo: {emergency_type}, Beneficiario: {beneficiary_name}")
    messagebox.showinfo("Emergencia Reportada", "Tu reporte de emergencia ha sido enviado.")

def start_user_interface():
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
                                  beneficiary_name_entry.get()))
    report_button.pack()

    window.mainloop()

if __name__ == "__main__":
    start_user_interface()
