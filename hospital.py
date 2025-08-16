import tkinter as tk
from tkinter import ttk, messagebox

# Main App Class
class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("900x600")
        self.root.config(bg="lightblue")

        # Title Label
        title = tk.Label(root, text="🏥 Hospital Management System", font=("Arial", 20, "bold"), bg="darkblue", fg="white")
        title.pack(side="top", fill="x")

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Tabs
        self.patient_tab = ttk.Frame(self.notebook)
        self.doctor_tab = ttk.Frame(self.notebook)
        self.appointment_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.patient_tab, text="Patients")
        self.notebook.add(self.doctor_tab, text="Doctors")
        self.notebook.add(self.appointment_tab, text="Appointments")

        # Call UI methods
        self.patient_ui()
        self.doctor_ui()
        self.appointment_ui()

        # Data Storage
        self.patients = []
        self.doctors = []
        self.appointments = []

    # Patient Tab
    def patient_ui(self):
        lbl = tk.Label(self.patient_tab, text="Patient Registration", font=("Arial", 16, "bold"))
        lbl.pack(pady=10)

        tk.Label(self.patient_tab, text="Name").pack()
        self.patient_name = tk.Entry(self.patient_tab)
        self.patient_name.pack()

        tk.Label(self.patient_tab, text="Age").pack()
        self.patient_age = tk.Entry(self.patient_tab)
        self.patient_age.pack()

        tk.Label(self.patient_tab, text="Gender").pack()
        self.patient_gender = ttk.Combobox(self.patient_tab, values=["Male", "Female", "Other"])
        self.patient_gender.pack()

        tk.Button(self.patient_tab, text="Add Patient", command=self.add_patient).pack(pady=5)

        self.patient_list = tk.Listbox(self.patient_tab, width=50, height=10)
        self.patient_list.pack(pady=10)

    def add_patient(self):
        name = self.patient_name.get()
        age = self.patient_age.get()
        gender = self.patient_gender.get()

        if name and age and gender:
            patient = f"{name} | Age: {age} | Gender: {gender}"
            self.patients.append(patient)
            self.patient_list.insert(tk.END, patient)
            messagebox.showinfo("Success", "Patient Added Successfully ✅")
        else:
            messagebox.showwarning("Error", "All fields are required!")

    # Doctor Tab
    def doctor_ui(self):
        lbl = tk.Label(self.doctor_tab, text="Doctor Management", font=("Arial", 16, "bold"))
        lbl.pack(pady=10)

        tk.Label(self.doctor_tab, text="Name").pack()
        self.doctor_name = tk.Entry(self.doctor_tab)
        self.doctor_name.pack()

        tk.Label(self.doctor_tab, text="Specialization").pack()
        self.doctor_specialization = tk.Entry(self.doctor_tab)
        self.doctor_specialization.pack()

        tk.Button(self.doctor_tab, text="Add Doctor", command=self.add_doctor).pack(pady=5)

        self.doctor_list = tk.Listbox(self.doctor_tab, width=50, height=10)
        self.doctor_list.pack(pady=10)

    def add_doctor(self):
        name = self.doctor_name.get()
        spec = self.doctor_specialization.get()

        if name and spec:
            doctor = f"{name} | Specialist in {spec}"
            self.doctors.append(doctor)
            self.doctor_list.insert(tk.END, doctor)
            messagebox.showinfo("Success", "Doctor Added Successfully ✅")
        else:
            messagebox.showwarning("Error", "All fields are required!")

    # Appointment Tab
    def appointment_ui(self):
        lbl = tk.Label(self.appointment_tab, text="Book Appointment", font=("Arial", 16, "bold"))
        lbl.pack(pady=10)

        tk.Label(self.appointment_tab, text="Select Patient").pack()
        self.app_patient = ttk.Combobox(self.appointment_tab, values=self.patients)
        self.app_patient.pack()

        tk.Label(self.appointment_tab, text="Select Doctor").pack()
        self.app_doctor = ttk.Combobox(self.appointment_tab, values=self.doctors)
        self.app_doctor.pack()

        tk.Button(self.appointment_tab, text="Book Appointment", command=self.book_appointment).pack(pady=5)

        self.appointment_list = tk.Listbox(self.appointment_tab, width=60, height=10)
        self.appointment_list.pack(pady=10)

    def book_appointment(self):
        patient = self.app_patient.get()
        doctor = self.app_doctor.get()

        if patient and doctor:
            appointment = f"Patient: {patient} -> Doctor: {doctor}"
            self.appointments.append(appointment)
            self.appointment_list.insert(tk.END, appointment)
            messagebox.showinfo("Success", "Appointment Booked ✅")
        else:
            messagebox.showwarning("Error", "Select Patient and Doctor!")


# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
