import sqlite3
from datetime import datetime

conn = sqlite3.connect('Hospital_Database.db')
cursor = conn.cursor()

# Create Patient table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Patient (
    PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    DOB DATE,
    Weight REAL,
    Height REAL,
    Gender TEXT,
    PhoneNo TEXT,
    EmailID TEXT,
    Address TEXT,
    MedicalHistory TEXT
)
''')

# Create Doctor table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Doctor (
    DoctorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    DOB DATE,
    Gender TEXT,
    Specialization TEXT,
    PhoneNo TEXT,
    EmailID TEXT,
    Address TEXT,
    AppointmentCost INTEGER,
    YearsOfExperience INTEGER,
    WorkStatus TEXT DEFAULT 'Active'
)
''')

# Create Bill table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Bill (
    BillID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER,
    BillType TEXT,
    Amount REAL,
    Date DATE,
    PaymentStatus TEXT DEFAULT 'Pending',
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
)
''')

# Create Room table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Room (
    RoomID INTEGER PRIMARY KEY AUTOINCREMENT,
    RoomType TEXT,
    AvailabilityStatus TEXT,
    Cost REAL
)
''')

# Create Leave table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Leave (
    LeaveID INTEGER PRIMARY KEY AUTOINCREMENT,
    DoctorID INTEGER,
    SelectDate DATE,
    ReturnDate DATE,
    NoOfDays INTEGER,
    Reason TEXT,
    LeaveStatus TEXT DEFAULT 'Pending',
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID)
)
''')

# Create Treatment table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Treatment (
    TreatmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER,
    DoctorID INTEGER,
    Diagnosis TEXT,
    TreatmentPlan TEXT,
    Medicines TEXT,
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID)
)
''')

# Create Medicine table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Medicine (
    MedicineID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Cost REAL,
    Use TEXT
)
''')

# Create Appointment table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Appointment (
    AppointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER,
    DoctorID INTEGER,
    Date DATE,
    Time TEXT,
    Purpose TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID)
)
''')

# Create LoginCredits table
cursor.execute('''
CREATE TABLE IF NOT EXISTS LoginCredits (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Password TEXT,
    UserType TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully.")

def insert_initial_data(conn):
    cursor = conn.cursor()
    
    # Insert data into Patient table with additional columns
    cursor.execute('''
    INSERT INTO Patient (Name, DOB, Weight, Height, Gender, PhoneNo, EmailID, Address, MedicalHistory)
    VALUES 
    ('John Doe', '1990-05-10', 75.5, 180, 'Male', '1234567890', 'john@example.com', '123 Main St', 'No known allergies'),
    ('Jane Smith', '1985-03-22', 65.2, 165, 'Female', '0987654321', 'jane@example.com', '456 Oak St', 'Asthma'),
    ('Michael Johnson', '1978-07-18', 82.4, 175, 'Male', '1122334455', 'michael.j@example.com', '789 Maple St', 'Diabetes Type II')
    ''')
    
    # Insert data into Doctor table with additional columns
    cursor.execute('''
    INSERT INTO Doctor (Name, DOB, Gender, Specialization, PhoneNo, EmailID, Address, AppointmentCost, YearsOfExperience, WorkStatus)
    VALUES 
    ('Dr. Emily Clark', '1975-09-15', 'Female', 'Cardiologist', '9876543210', 'emily@hospital.com', '789 Pine St', 800, 15, 'Active'),
    ('Dr. Robert Brown', '1980-11-12', 'Male', 'Neurologist', '8765432109', 'robert@hospital.com', '321 Elm St', 500, 10, 'Active'),
    ('Dr. Susan Miller', '1972-03-05', 'Female', 'Orthopedist', '9988776655', 'susan@hospital.com', '654 Birch St', 1000, 20, 'Active')
    ''')
    
    # Insert data into Bill table
    cursor.execute('''
    INSERT INTO Bill (PatientID, BillType, Amount, Date, PaymentStatus)
    VALUES 
    (1, 'Consultation', 100.0, '2024-10-01', 'Paid'),
    (2, 'Medicines', 250.5, '2024-10-05', 'Pending'),
    (3, 'Surgery', 5000.0, '2024-09-25', 'Paid')
    ''')
    
    # Insert data into Room table with additional columns
    cursor.execute('''
    INSERT INTO Room (RoomType, AvailabilityStatus, Cost)
    VALUES 
    ('General', 'Available', 500.0),
    ('ICU', 'Occupied', 2000.0),
    ('Deluxe', 'Available', 1500.0)
    ''')

    # Insert data into Leave table
    cursor.execute('''
    INSERT INTO Leave (DoctorID, SelectDate, ReturnDate, NoOfDays, Reason, LeaveStatus)
    VALUES 
    (1, '2024-11-01', '2024-11-10', 10, 'Medical Leave', 'Approved'),
    (2, '2024-12-01', '2024-12-05', 5, 'Vacation', 'Pending')
    ''')

    # Insert data into Treatment table
    cursor.execute('''
    INSERT INTO Treatment (PatientID, DoctorID, Diagnosis, TreatmentPlan, Medicines, StartDate, EndDate)
    VALUES 
    (1, 1, 'Hypertension', 'Lifestyle changes and medication', 'Lisinopril', '2024-10-01', '2024-11-01'),
    (2, 2, 'Migraine', 'Pain management', 'Ibuprofen', '2024-10-05', '2024-11-05'),
    (3, 3, 'Knee Injury', 'Surgery and physiotherapy', 'Paracetamol', '2024-09-25', '2024-12-25')
    ''')

    # Insert data into Medicine table with additional columns
    cursor.execute('''
    INSERT INTO Medicine (Name, Cost, Use)
    VALUES 
    ('Lisinopril', 10.5, 'Blood pressure control'),
    ('Ibuprofen', 5.0, 'Pain relief'),
    ('Paracetamol', 2.0, 'Pain and fever relief'),
    ('Amoxicillin', 15.0, 'Antibiotic')
    ''')

    # Insert data into Appointment table
    cursor.execute('''
    INSERT INTO Appointment (PatientID, DoctorID, Date, Time, Purpose)
    VALUES 
    (1, 1, '2024-10-15', '10:00 AM', 'Follow-up on hypertension'),
    (2, 2, '2024-10-20', '2:00 PM', 'Migraine consultation'),
    (3, 3, '2024-11-05', '11:30 AM', 'Post-surgery checkup')
    ''')

    # Insert data into LoginCredits table
    cursor.execute('''
    INSERT INTO LoginCredits (UserID, Password, UserType)
    VALUES 
    (1, 'password123', 'Patient'),
    (2, 'securepass456', 'Doctor'),
    (3, 'adminpass789', 'Admin')
    ''')

    # Commit the transaction
    conn.commit()

    print("Initial data inserted successfully.")

import sqlite3
from sqlite3 import Error

def create_connection():
    """Create a database connection to the SQLite database specified."""
    try:
        conn = sqlite3.connect('Hospital_Database.db')  # Change 'hospital.db' to the desired database file name
        print("Connection established successfully")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

#enable the following comments for input data in database
#conn = create_connection()
#insert_initial_data(conn)

import sqlite3
from datetime import datetime, date

def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

def create_connection():
    return sqlite3.connect('Hospital_Database.db')

def execute_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    return cursor

def fetch_data(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

def main():
    conn = create_connection()
    
    while True:
        print("\nWelcome to Amrita Hospital")
        print("1. Login")
        print("2. Sign in (for Patients only)")
        print("3. Hospital info")
        print("4. Exit")
        
        choice = input("Enter: ")
        
        if choice == '1':
            login(conn)
        elif choice == '2':
            sign_in(conn)
        elif choice == '3':
            hospital_info(conn)
        elif choice == '4':
            print("Thank you for visiting our hospital. Come back again!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")
    
    conn.close()
    
def login(conn):
    while True:
        print("\nSelect User")
        print("1. Doctor")
        print("2. Patient")
        print("3. Admin")
        user_type = input("Enter: ")
                
        if user_type in ['1', '2', '3']:
            user_type = ['Doctor', 'Patient', 'Admin'][int(user_type) - 1]
        else:
            print("Invalid user type.")
            break
        
        user_id = input("Enter UserID: ")
        password = input("Enter Password: ")
        
        query = "SELECT * FROM LoginCredits WHERE UserID = ? AND Password = ? AND UserType = ?"
        result = fetch_data(conn, query, (user_id, password, user_type))
        
        if result:
            if user_type == 'Doctor':
                doctor_function(conn, user_id)
            elif user_type == 'Patient':
                patient_function(conn, user_id)
            elif user_type == 'Admin':
                admin_function(conn, user_id)
        else:
            print("Invalid credentials.")
        break
        
def sign_in(conn):
    password = input("Enter Password: ")

    execute_query(conn, "INSERT INTO LoginCredits (Password, UserType) VALUES (?, ?)", (password, 'Patient'))

    cursor = conn.cursor()
    cursor.execute("SELECT last_insert_rowid()")
    user_id = cursor.fetchone()[0]

    print(f"Your UserID (also your PatientID) is: {user_id}")

    name = input("Name: ")
    dob = datetime.strptime(input("DOB (dd/mm/yyyy): "), "%d/%m/%Y").date()
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    gender = input("Gender: ")
    phone = input("Phone no: ")
    email = input("Email id: ")
    address = input("Address: ")
    medical_history = input("Medical History: ")

    execute_query(conn, """
    INSERT INTO Patient (PatientID, Name, DOB, Weight, Height, Gender, PhoneNo, EmailID, Address, MedicalHistory)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, name, dob, weight, height, gender, phone, email, address, medical_history))

    print("Sign-in successful and patient details recorded.")
    
def hospital_info(conn):
    print("Contact no: 8498982104")
    print("Email: amritahosptal1990@gmail.com")
    print("Address: Amritapuri, Kochi")
    print("Timing: 24 hours doctor availability 10:00 to 5:00")
    query = "SELECT DISTINCT Specialization FROM doctor"
    specialists = fetch_data(conn, query)
    print("Specialists:")
    if specialists:
        for specialist in specialists:
            print(f"- {specialist[0]}s")
    else:
        print("No specialists available.")


def doctor_function(conn, doctor_id):
    while True:
        print("\n1. My profile")
        print("2. View Doctors")
        print("3. View Patients")
        print("4. My Patients")
        print("5. My Appointments")
        print("6. View Patient's Treatment info")
        print("7. Apply leave")
        print("8. Edit password")
        print("9. Exit")
        choice = input("Enter your option: ")
        
        if choice == '1':
            my_profile(conn, doctor_id)
        elif choice == '2':
            view_doctors(conn)
        elif choice == '3':
            view_patients(conn)
        elif choice == '4':
            my_patients(conn, doctor_id)
        elif choice == '5':
            my_appointments(conn, doctor_id)
        elif choice == '6':
            view_patient_treatment_info(conn, doctor_id)
        elif choice == '7':
            apply_leave(conn, doctor_id)
        elif choice == '8':
            edit_password(conn, doctor_id)
        elif choice == '9':
            break
        else:
            print("Invalid option. Please enter a number between 1 and 11.")

def my_profile(conn, doctor_id):
    query = "SELECT * FROM Doctor WHERE DoctorID = ?"
    result = fetch_data(conn, query, (doctor_id,))
    
    if result:
        print('=========== MY PROFILE ===========')
        doctor = result[0]
        print(f"DoctorID: {doctor[0]}")
        print(f"Name: {doctor[1]}")
        print(f"Age: {calculate_age(datetime.strptime(doctor[2], '%Y-%m-%d').date())}")
        print(f"DOB: {doctor[2]}")
        print(f"Gender: {doctor[3]}")
        print(f"Specialization: {doctor[4]}")
        print(f"Phone no: {doctor[5]}")
        print(f"Email id: {doctor[6]}")
        print(f"Address: {doctor[7]}")
        print(f"Appointment cost: {doctor[8]}")
        print(f"Years of Experience: {doctor[9]}")
        print(f"Work Status: {doctor[10]}")
        
        while True:
            print("\n1. Edit info")
            print("2. Back")
            print("3. Exit")
            choice = input("Enter your option: ")
            
            if choice == '1':
                edit_info(conn, doctor_id)
            elif choice == '2':
                break
            elif choice == '3':
                exit()
            else:
                print("Invalid option. Please enter a number between 1 and 3.")
    else:
        print("Doctor not found.")

def edit_info(conn, doctor_id):
    while True:
        print("\n1. Phone no")
        print("2. Email id")
        print("3. Address")
        choice = input("Enter your option: ")
        
        if choice in ['1', '2', '3']:
            new_value = input("Enter new value: ")
            field = {
                '1': 'PhoneNo',
                '2': 'EmailID',
                '3': 'Address'
            }[choice]
            
            execute_query(conn, f"UPDATE Doctor SET {field} = ? WHERE DoctorID = ?", (new_value, doctor_id))
            print("Information updated successfully.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 3.")

def view_doctors(conn):
    query = "SELECT DoctorID, Name, Specialization FROM Doctor ORDER BY Specialization"
    doctors = fetch_data(conn, query)
    
    for doctor in doctors:
        print(f"DoctorID: {doctor[0]}, Name: {doctor[1]}, Specialization: {doctor[2]}")
    
    while True:
        print("\n1. Search by Attribute")
        print("2. View doctor info")
        print("3. Back")
        print("4. Exit")
        choice = input("Enter your option: ")
        
        if choice == '1':
            search_doctor_by_attribute(conn)
        elif choice == '2':
            view_doctor_info(conn)
        elif choice == '3':
            break
        elif choice == '4':
            exit()
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

def search_doctor_by_attribute(conn):
    attributes = ['DoctorID', 'Name', 'Age', 'DOB', 'Gender', 'Specialization', 'PhoneNo', 'EmailID', 'YearsOfExperience', 'WorkStatus']
    
    for i, attr in enumerate(attributes, 1):
        print(f"{i}. {attr}")
    
    choice = input("Enter your option: ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(attributes):
        attr = attributes[int(choice) - 1]
        search_value = input(f"Search by {attr}: ")
        
        query = f"SELECT * FROM Doctor WHERE {attr} LIKE ?"
        results = fetch_data(conn, query, (f"%{search_value}%",))
        
        if results:
            for doctor in results:
                print(doctor)
        else:
            print("Not found")
    else:
        print(f"Invalid option. Please enter a number between 1 and {len(attributes)}.")

def view_doctor_info(conn):
    doctor_id = input("Enter DoctorID: ")
    query = "SELECT * FROM Doctor WHERE DoctorID = ?"
    result = fetch_data(conn, query, (doctor_id,))
    
    if result:
        doctor = result[0]
        print(f"DoctorID: {doctor[0]}")
        print(f"Name: {doctor[1]}")
        print(f"Age: {calculate_age(datetime.strptime(doctor[2], '%Y-%m-%d').date())}")
        print(f"DOB: {doctor[2]}")
        print(f"Gender: {doctor[3]}")
        print(f"Specialization: {doctor[4]}")
        print(f"Phone no: {doctor[5]}")
        print(f"Email id: {doctor[6]}")
        print(f"Address: {doctor[7]}")
        print(f"Appointment cost: {doctor[8]}")
        print(f"Years of Experience: {doctor[9]}")
        print(f"Work Status: {doctor[10]}")
    else:
        print("Doctor not found.")

def view_patients(conn):
    query = "SELECT PatientID, Name, DOB FROM Patient ORDER BY Name"
    patients = fetch_data(conn, query)
    
    for patient in patients:
        print(f"PatientID: {patient[0]}, Name: {patient[1]}, DOB: {patient[2]}")
    
    while True:
        print("\n1. Search by Attribute")
        print("2. View patient info")
        print("3. Back")
        print("4. Exit")
        choice = input("Enter your option: ")
        
        if choice == '1':
            search_patient_by_attribute(conn)
        elif choice == '2':
            patient_id = input("Enter PatientID: ")
            view_patient_info(conn, patient_id)
        elif choice == '3':
            break
        elif choice == '4':
            exit()
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

def search_patient_by_attribute(conn):
    attributes = ['PatientID', 'Name', 'DOB', 'Gender', 'PhoneNo', 'EmailID', 'Weight', 'Height', 'MedicalHistory']
    
    for i, attr in enumerate(attributes, 1):
        print(f"{i}. {attr}")
    
    choice = input("Enter your option: ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(attributes):
        attr = attributes[int(choice) - 1]
        search_value = input(f"Search by {attr}: ")
        
        query = f"SELECT * FROM Patient WHERE {attr} LIKE ?"
        results = fetch_data(conn, query, (f"%{search_value}%",))
        
        if results:
            for patient in results:
                print(patient)
        else:
            print("Not found.")
    else:
        print(f"Invalid option. Please enter a number between 1 and {len(attributes)}.")

def view_patient_info(conn, patient_id):
    query = "SELECT * FROM Patient WHERE PatientID = ?"
    result = fetch_data(conn, query, (patient_id,))
    
    if result:
        patient = result[0]
        print(f"PatientID: {patient[0]}")
        print(f"Name: {patient[1]}")
        print(f"DOB: {patient[2]}")
        print(f"Weight: {patient[3]}")
        print(f"Height: {patient[4]}")
        print(f"Gender: {patient[5]}")
        print(f"Phone no: {patient[6]}")
        print(f"Email id: {patient[7]}")
        print(f"Address: {patient[8]}")
        print(f"Medical History: {patient[9]}")
    else:
        print("Patient not found.")

def my_patients(conn, doctor_id):
    query = """
    SELECT DISTINCT p.* 
    FROM Patient p
    JOIN Treatment t ON p.PatientID = t.PatientID
    WHERE t.DoctorID = ?
    """
    patients = fetch_data(conn, query, (doctor_id,))
    
    for patient in patients:
        print(f"PatientID: {patient[0]}, Name: {patient[1]}")

import sqlite3
from datetime import datetime, date, timedelta

def view_patient_treatment_info(conn, doctor_id):
    
    while True:
        print("\n1. Search by patientId")
        print("2. Search by treatmentId")
        print("3. Back")
        print("4. Exit")
        choice = input("Enter your option: ")
        
        if choice == '1':
            treatment_info(conn, 'PatientID', doctor_id)
        elif choice == '2':
            treatment_info(conn, 'TreatmentID', doctor_id)
        elif choice == '3':
            break
        elif choice == '4':
            exit()
        else:
            print("Invalid option. Please enter a number between 1 and 4.")


def treatment_info(conn, search_column, doctor_id):
    
    query = f"""
    SELECT * FROM Treatment WHERE {search_column} = ?
    """
    search_id=input(f'Enter the {search_column}:')
    treatment = fetch_data(conn, query, (search_id,))
    if treatment:
        treatment = treatment[0]
        print(f"TreatmentID: {treatment[0]}")
        print(f"PatientID: {treatment[1]}")
        print(f"DoctorID: {treatment[2]}")
        print(f"Diagnosis: {treatment[3]}")
        print(f"Medicines: {treatment[4]}")
        print(f"TreatmentPlan: {treatment[5]}")
        print(f"StartDate: {treatment[6]}")
        print(f"EndDate: {treatment[7]}")
    else:
        print("Treatment not found.")
        
    while True:
        print("\n1. Edit Treatment")
        print("2. Back")
        choice = input("Enter your option: ")
        
        if choice == '1':
            edit_treatment(conn, doctor_id, treatment[0])
        elif choice == '2':
            break
        else:
            print("Invalid option. Please enter a number between 1 or 2.")

def edit_treatment(conn, doctor_id, treatment_id):
    
    result = fetch_data(conn, "SELECT * FROM Treatment WHERE TreatmentID = ? AND DoctorID = ?", (treatment_id, doctor_id))
    
    if not result:
        print("TreatmentID not found or you are not authorized to edit this record.")
        return
    
    options = {
        '1': 'Diagnosis',
        '2': 'Medicines',
        '3': 'TreatmentPlan',
        '4': 'StartDate',
        '5': 'EndDate'
    }
    
    print("\n".join([f"{k}. {v}" for k, v in options.items()]))
    choice = input("Enter your option: ")
    
    if choice in options:
        new_value = input(f"Enter new {options[choice]}: ")
        execute_query(conn, f"UPDATE Treatment SET {options[choice]} = ? WHERE TreatmentID = ?", (new_value, treatment_id))
        print("Treatment updated successfully.")
    else:
        print("Invalid option.")

def my_appointments(conn, doctor_id):
    query = """
    SELECT a.AppointmentID, a.PatientID, a.Date, a.Time, p.Name, p.DOB, p.Gender
    FROM Appointment a
    JOIN Patient p ON a.PatientID = p.PatientID
    WHERE a.DoctorID = ?
    ORDER BY a.Date, a.Time
    """
    appointments = fetch_data(conn, query, (doctor_id,))
    
    # Check if there are no appointments
    if not appointments:  # If appointments is empty
        print("You have no Appointments.")
        return  # Exit the function if there are no appointments
    
    # Displaying the appointment and patient information
    for appointment in appointments:
        patient_dob = datetime.strptime(appointment[5], '%Y-%m-%d').date()  # Assuming p.DOB is at index 5
        age = calculate_age(patient_dob)
        print(f"AppointmentID: {appointment[0]}, PatientID: {appointment[1]}, Name: {appointment[4]}, Age: {age}, Gender: {appointment[6]}, Time: {appointment[3]}, Date: {appointment[2]}")
    
    print("-------------------------------------")
    
    # Menu options after showing appointments
    while True:
        print("1. View Patient's info")
        print("2. Start Treatment")
        print("3. Back")
        print("4. Exit")
        choice = input("Enter your option: ")
        
        if choice == '1':
            patient_id = input("Enter PatientID: ")
            view_patient_info(conn, patient_id)
        elif choice == '2':
            start_treatment(conn, doctor_id)
        elif choice == '3':
            # If Back is selected, go to the doctor menu (assuming this is defined)
            doctor_function(conn, doctor_id)  # Assuming this function returns to the doctor's main menu
            break
        elif choice == '4':
            exit()
        else:
            print("Enter number from 1-4")


def start_treatment(conn, doctor_id):
    appointment_id = input("Enter AppointmentID: ")
    
    # Check if the appointment exists and belongs to the doctor
    result = fetch_data(conn, "SELECT * FROM Appointment WHERE AppointmentID = ? AND DoctorID = ?", (appointment_id, doctor_id))
    
    if not result:
        print("AppointmentID not found or you are not appointed to this patient.")
        return
    
    appointment = result[0]
    patient_id = appointment[1]
    purpose = appointment[4]
    
    view_patient_info(conn, patient_id)
    
    print(f"\nPurpose of Appointment: {purpose}")
    
    # Start the treatment process
    diagnosis = input("\nDiagnosis: ")
    medicines = input("Medicines: ")
    treatment_plan = input("Treatment Plan: ")
    start_date = input("Start Date (dd/mm/yyyy): ")
    end_date = input("End Date (dd/mm/yyyy): ")
    
    # Insert the treatment data into the Treatment table
    execute_query(conn, """
    INSERT INTO Treatment (PatientID, DoctorID, Diagnosis, Medicines, TreatmentPlan, StartDate, EndDate)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (patient_id, doctor_id, diagnosis, medicines, treatment_plan, start_date, end_date))
    
    print("\nTreatment started successfully.")
    
    # Delete the appointment from the Appointment table after treatment
    execute_query(conn, "DELETE FROM Appointment WHERE AppointmentID = ?", (appointment_id,))
    
    print("Appointment record deleted after treatment.")

def apply_leave(conn, doctor_id):
    today = date.today()
    min_leave_date = today + timedelta(weeks=3)
    
    while True:
        select_date = input(f"Select date (dd/mm/yyyy, must be after {min_leave_date.strftime('%d/%m/%Y')}): ")
        select_date = datetime.strptime(select_date, "%d/%m/%Y").date()
        
        if select_date > min_leave_date:
            break
        else:
            print("Invalid date. Please select a date at least 3 weeks from today.")
    
    return_date = input("Return date (dd/mm/yyyy): ")
    return_date = datetime.strptime(return_date, "%d/%m/%Y").date()
    reason = input("Reason: ")
    
    no_of_days = (return_date - select_date).days + 1
    
    execute_query(conn, """
    INSERT INTO Leave (DoctorID, SelectDate, ReturnDate, NoOfDays, Reason, LeaveStatus)
    VALUES (?, ?, ?, ?, ?, 'Pending')
    """, (doctor_id, select_date, return_date, no_of_days, reason))
    
    print("Leave application submitted successfully.")

def edit_password(conn, user_id):
    new_password = input("Enter new password: ")
    execute_query(conn, "UPDATE LoginCredits SET Password = ? WHERE UserID = ?", (new_password, user_id))
    print("Password updated successfully.")
    input("\nPress Enter to continue...")

import sqlite3
from datetime import datetime, date, timedelta
import calendar


def patient_function(conn, patient_id):
    while True:
        print("\n1. My profile")
        print("2. Appointments")
        print("3. Bills")
        print("4. Book Room")
        print("5. Buy Medicines")
        print("6. Edit password")
        print("7. Exit")
        choice = input("Enter your option: ")
        
        if choice == '1':
            patient_profile(conn, patient_id)
        elif choice == '2':
            patient_appointments(conn, patient_id)
        elif choice == '3':
            patient_bills(conn, patient_id)
        elif choice == '4':
            book_room(conn, patient_id)
        elif choice == '5':
            buy_medicines(conn, patient_id)
        elif choice == '6':
            edit_password(conn, patient_id)
        elif choice == '7':
            print("Thank you for visiting our hospital. Come back again!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 7.")

def patient_profile(conn, patient_id):
    query = "SELECT * FROM Patient WHERE PatientID = ?"
    result = fetch_data(conn, query, (patient_id,))
    
    if result:
        print('=========== MY PROFILE ===========')
        patient = result[0]
        print(f"PatientID: {patient[0]}")
        print(f"Name: {patient[1]}")
        print(f"Age: {calculate_age(datetime.strptime(patient[2], '%Y-%m-%d').date())}")
        print(f"DOB: {patient[2]}")
        print(f"Weight: {patient[3]}")
        print(f"Height: {patient[4]}")
        print(f"Gender: {patient[5]}")
        print(f"Phone no: {patient[6]}")
        print(f"Email id: {patient[7]}")
        print(f"Address: {patient[8]}")
        print(f"Medical History: {patient[9]}")
        print("-------------------------------------")
        
        while True:
            print("1. Edit info")
            print("2. Back")
            print("3. Exit")
            choice = input("Enter your option: ")
            
            if choice == '1':
                edit_patient_info(conn, patient_id)
            elif choice == '2':
                break
            elif choice == '3':
                exit()
            else:
                print("Invalid option. Please enter a number between 1 and 3.")
    else:
        print("Patient not found.")

def edit_patient_info(conn, patient_id):
    while True:
        print("1. Phone no")
        print("2. Email id")
        print("3. Address")
        choice = input("Enter your option: ")
        
        if choice in ['1', '2', '3']:
            field = ['PhoneNo', 'EmailID', 'Address'][int(choice) - 1]
            new_value = input(f"Enter new {field}: ")
            execute_query(conn, f"UPDATE Patient SET {field} = ? WHERE PatientID = ?", (new_value, patient_id))
            print("Information updated successfully.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 3.")

def patient_appointments(conn, patient_id):
    while True:
        print("1. My Appointments")
        print("2. Book Appointment")
        print("3. Back")
        choice = input("Enter your option: ")
        
        if choice == '1':
            view_patient_appointments(conn, patient_id)
        elif choice == '2':
            book_appointment(conn, patient_id)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please enter a number between 1 and 2.")

def view_patient_appointments(conn, patient_id):
    query = """
    SELECT a.*, d.Name as DoctorName
    FROM Appointment a
    JOIN Doctor d ON a.DoctorID = d.DoctorID
    WHERE a.PatientID = ?
    ORDER BY a.Date, a.Time
    """
    appointments = fetch_data(conn, query, (patient_id,))
    
    for appointment in appointments:
        print(f"AppointmentID: {appointment[0]}, Doctor: {appointment[5]}, Date: {appointment[3]}, Time: {appointment[4]}")
    
    print("-------------------------------------")
    while True:
        print("1. View Doctor's info")
        print("2. Back")
        print("3. Exit")
        choice = input("Enter your option: ")
        
        if choice == '1':
            doctor_id = input("Enter DoctorID: ")
            view_doctor_info(conn, doctor_id)
        elif choice == '2':
            break
        elif choice == '3':
            exit()
        else:
            print("Enter number from 1-3")

def book_appointment(conn, patient_id):
    active_doctors = fetch_data(conn, "SELECT DoctorID, Name, Specialization FROM Doctor WHERE WorkStatus = 'Active' ORDER BY Specialization")
    for doctor in active_doctors:
        print(f"DoctorID: {doctor[0]}, Name: {doctor[1]}, Specialization: {doctor[2]}")
    
    print("----------------------------------------------------------------------------------------------------")
 
    while True:
        print("\n=== Book Appointment ===")
        print("1. Search Doctor Directly")
        print("2. Browse Doctors by Specialization")
        print("3. Back")
        choice = input("Enter your option: ")
        
        if choice == '1':
            select_doctor(conn, patient_id)
        elif choice == '2':
            select_doctors_by_specialization(conn, patient_id)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please enter a number between 1 and 3.")


def select_doctors_by_specialization(conn, patient_id):
    specializations = fetch_data(conn, "SELECT DISTINCT Specialization FROM Doctor WHERE WorkStatus = 'Active'")
    
    while True:
        print("\n=== Available Specializations ===")
        for i, spec in enumerate(specializations, 1):
            print(f"{i}. {spec[0]}")
        print(f"{len(specializations) + 1}. Back")
        
        try:
            choice = int(input("\nSelect specialization number: "))
            if choice == len(specializations) + 1:
                break
            elif 1 <= choice <= len(specializations):
                selected_spec = specializations[choice - 1][0]
                
                # Updated query to include AppointmentCost
                doctors = fetch_data(conn, """
                    SELECT DoctorID, Name, YearsOfExperience, AppointmentCost 
                    FROM Doctor 
                    WHERE Specialization = ? AND WorkStatus = 'Active'
                    ORDER BY Name
                """, (selected_spec,))
                
                print(f"\n=== Doctors specialized in {selected_spec} ===")
                for doctor in doctors:
                    print(f"ID: {doctor[0]}, Name: {doctor[1]}, Experience: {doctor[2]} years, Consultation Fee: ${doctor[3]:.2f}")
                
                while True:
                    print("\n1. Select Doctor")
                    print("2. Back to Specializations")
                    subchoice = input("Enter your option: ")
                    
                    if subchoice == '1':
                        doctor_id = input("Enter Doctor ID to proceed: ")
                        doctor_check = fetch_data(conn, """
                            SELECT DoctorID, AppointmentCost FROM Doctor 
                            WHERE DoctorID = ? AND Specialization = ? AND WorkStatus = 'Active'
                        """, (doctor_id, selected_spec))
                        
                        if doctor_check:
                            proceed_with_appointment(conn, patient_id, doctor_id, doctor_check[0][1])
                            return
                        else:
                            print("Invalid Doctor ID. Please try again.")
                    elif subchoice == '2':
                        break
                    else:
                        print("Invalid option. Please enter 1 or 2.")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def select_doctor(conn, patient_id):
    while True:
        print("\n=== Search Doctor ===")
        print("1. Search by ID")
        print("2. Search by Name")
        print("3. Back")
        choice = input("Enter your option: ")
        
        if choice == '3':
            break
            
        if choice in ['1', '2']:
            search_term = input("Enter search term: ")
            
            if choice == '1':
                query = """
                    SELECT DoctorID, Name, Specialization, YearsOfExperience, AppointmentCost 
                    FROM Doctor 
                    WHERE DoctorID = ? AND WorkStatus = 'Active'
                """
                params = (search_term,)
            else:  # choice == '2'
                query = """
                    SELECT DoctorID, Name, Specialization, YearsOfExperience, AppointmentCost 
                    FROM Doctor 
                    WHERE Name LIKE ? AND WorkStatus = 'Active'
                """
                params = (f"%{search_term}%",)
            
            doctors = fetch_data(conn, query, params)
            
            if doctors:
                print("\n=== Matching Doctors ===")
                for doctor in doctors:
                    print(f"ID: {doctor[0]}, Name: {doctor[1]}, Specialization: {doctor[2]}, "
                          f"Experience: {doctor[3]} years, Consultation Fee: ${doctor[4]:.2f}")
                
                while True:
                    print("\n1. Select Doctor")
                    print("2. New Search")
                    subchoice = input("Enter your option: ")
                    
                    if subchoice == '1':
                        doctor_id = input("Enter Doctor ID to proceed: ")
                        doctor_check = fetch_data(conn, """
                            SELECT DoctorID, AppointmentCost FROM Doctor 
                            WHERE DoctorID = ? AND WorkStatus = 'Active'
                        """, (doctor_id,))
                        
                        if doctor_check:
                            proceed_with_appointment(conn, patient_id, doctor_id, doctor_check[0][1])
                            return
                        else:
                            print("Invalid Doctor ID. Please try again.")
                    elif subchoice == '2':
                        break
                    else:
                        print("Invalid option. Please enter 1 or 2.")
            else:
                print("No matching doctors found.")
        else:
            print("Invalid option. Please enter a number between 1 and 3.")

def is_date_available(conn, doctor_id, date):
    """
    Check if there are any available slots on a given date for a doctor
    Returns True if slots are available, False if fully booked
    """
    # Get all booked appointments for the doctor on the given date
    booked_times = fetch_data(conn, """
        SELECT Time 
        FROM Appointment 
        WHERE DoctorID = ? AND Date = ?
    """, (doctor_id, date))
    
    # Convert booked_times to a list of time strings
    booked_slots = [appointment[0] for appointment in booked_times]
    
    # Get all possible time slots (9 AM to 5 PM, 1-hour slots)
    all_slots = [f"{hour:02d}:00" for hour in range(9, 17)]
    
    # Check if there are any available slots
    return any(slot not in booked_slots for slot in all_slots)

def get_available_slots(conn, doctor_id, date):
    """
    Get list of available time slots for a given doctor and date
    """
    # Get all booked appointments for the doctor on the given date
    booked_times = fetch_data(conn, """
        SELECT Time 
        FROM Appointment 
        WHERE DoctorID = ? AND Date = ?
    """, (doctor_id, date))
    
    # Convert booked_times to a list of time strings
    booked_slots = [appointment[0] for appointment in booked_times]
    
    # Define all possible time slots (9 AM to 5 PM, 1-hour slots)
    all_slots = [f"{hour:02d}:00" for hour in range(9, 17)]
    
    # Return only available slots
    return [slot for slot in all_slots if slot not in booked_slots]

def proceed_with_appointment(conn, patient_id, doctor_id, appointment_cost):
    today = date.today()
    
    print("\n=== Available Dates ===")
    available_dates = []
    
    # Check availability for next 21 days
    for i in range(21):  # Next 3 weeks
        current_date = today + timedelta(days=i)
        is_available = is_date_available(conn, doctor_id, current_date)
        date_str = current_date.strftime("%Y-%m-%d")
        
        # Store available dates and display status
        if is_available:
            available_dates.append(current_date)
            print(f"{date_str} - Available")
        else:
            print(f"{date_str} - Fully Booked")
    
    if not available_dates:
        print("\nNo available slots in the next 3 weeks. Please try another doctor.")
        return
    
    while True:
        print("\nPlease select from available dates only.")
        selected_date = input("Select date (YYYY-MM-DD): ")
        try:
            selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
            if selected_date in available_dates:
                break
            elif today <= selected_date <= today + timedelta(weeks=3):
                print("This date is fully booked. Please select an available date.")
            else:
                print("Please select a date within the next 3 weeks.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    # Get available time slots
    available_slots = get_available_slots(conn, doctor_id, selected_date)
    
    if not available_slots:
        print("No available time slots for this date. Please select another date.")
        return
    
    print("\n=== Available Time Slots ===")
    for i, slot in enumerate(available_slots, 1):
        print(f"{i}. {slot}")
    
    while True:
        try:
            slot_choice = int(input("\nSelect time slot number: "))
            if 1 <= slot_choice <= len(available_slots):
                selected_time = available_slots[slot_choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(available_slots)}")
        except ValueError:
            print("Please enter a valid number.")
    
    # Double-check if slot is still available before booking
    if selected_time in get_available_slots(conn, doctor_id, selected_date):
        try:
            # Start transaction
            conn.execute("BEGIN TRANSACTION")
            
            # Insert the appointment
            execute_query(conn, """
            INSERT INTO Appointment (PatientID, DoctorID, Date, Time, Purpose)
            VALUES (?, ?, ?, ?, ?)
            """, (patient_id, doctor_id, selected_date, selected_time, "Regular checkup"))
            
            # Create the corresponding bill
            execute_query(conn, """
            INSERT INTO Bill (PatientID, BillType, Amount, Date, PaymentStatus)
            VALUES (?, 'Appointment', ?, ?, 'Pending')
            """, (patient_id, appointment_cost, selected_date))
            
            # Commit transaction
            conn.commit()
            
            print("\n=== Appointment Booked Successfully! ===")
            print(f"Date: {selected_date}")
            print(f"Time: {selected_time}")
            print(f"Consultation Fee: ${appointment_cost:.2f}")
            print("A bill has been generated for your appointment.")
            
            # Get doctor's name for confirmation
            doctor_name = fetch_data(conn, "SELECT Name FROM Doctor WHERE DoctorID = ?", (doctor_id,))[0][0]
            print(f"Doctor: {doctor_name}")
            
        except Exception as e:
            # Rollback in case of error
            conn.rollback()
            print("Error booking appointment. Please try again.")
            print(f"Error details: {str(e)}")
    else:
        print("Sorry, this slot has just been booked by another patient. Please try another slot.")

        
def is_date_available(conn, doctor_id, date):
    query = "SELECT COUNT(*) FROM Appointment WHERE DoctorID = ? AND Date = ?"
    result = fetch_data(conn, query, (doctor_id, date))
    return result[0][0] < 14  # Assuming 14 slots per day

def get_available_slots(conn, doctor_id, date):
    all_slots = ["10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30"]
    query = "SELECT Time FROM Appointment WHERE DoctorID = ? AND Date = ?"
    booked_slots = [row[0] for row in fetch_data(conn, query, (doctor_id, date))]
    return [slot for slot in all_slots if slot not in booked_slots]

def patient_bills(conn, patient_id):
    query = "SELECT BillID, Amount, BillType, Date, PaymentStatus FROM Bill WHERE PatientID = ?"
    bills = fetch_data(conn, query, (patient_id,))
    
    for bill in bills:
        print(f"BillID: {bill[0]}, Amount: {bill[1]}, Bill Type:{bill[2]}, Date: {bill[3]}, Payment Status: {bill[4]}")
    
    while True:
        print("1. View unpaid bills")
        print("2. Back")
        print("3. Exit")
        choice = input("Enter your option: ")
        
        if choice == '1':
            view_unpaid_bills(conn, patient_id)
        elif choice == '2':
            break
        elif choice == '3':
            exit()
        else:
            print("Invalid option. Please enter a number between 1 and 3.")

def view_unpaid_bills(conn, patient_id):
    query = "SELECT BillID, Amount, BillType, Date FROM Bill WHERE PatientID = ? AND PaymentStatus = 'Pending'"
    unpaid_bills = fetch_data(conn, query, (patient_id,))
    
    for bill in unpaid_bills:
        print(f"BillID: {bill[0]}, Amount: {bill[1]}, Bill Type:{bill[2]}, Date: {bill[3]}")
    
    while True:
        print("1. Pay Bill")
        print("2. Back")
        choice = input("Enter your option: ")
        
        if choice == '1':
            pay_bill(conn, patient_id)
        elif choice == '2':
            break
        else:
            print("Invalid option. Please enter 1 or 2.")

def pay_bill(conn, patient_id):
    bill_id = input("Enter the BillID: ")
    query = "SELECT Amount FROM Bill WHERE BillID = ? AND PatientID = ? AND PaymentStatus = 'Pending'"
    result = fetch_data(conn, query, (bill_id, patient_id))
    
    if result:
        amount = result[0][0]
        confirm = input(f"Do you accept to pay ${amount}? [y/n]: ")
        if confirm.lower() == 'y':
            execute_query(conn, "UPDATE Bill SET PaymentStatus = 'Paid' WHERE BillID = ?", (bill_id,))
            print("Bill paid successfully.")
        else:
            print("Payment cancelled.")
    else:
        print("Invalid BillID or bill is already paid.")

def book_room(conn, patient_id):
    room_types = fetch_data(conn, "SELECT DISTINCT RoomType FROM Room")
    for i, room_type in enumerate(room_types, 1):
        print(f"{i}. {room_type[0]}")
    
    choice = input("Enter Room Type (Enter the labeled number): ")
    if choice.isdigit() and 1 <= int(choice) <= len(room_types):
        selected_room_type = room_types[int(choice) - 1][0]
        available_rooms = fetch_data(conn, 
            "SELECT RoomID, Cost FROM Room WHERE RoomType = ? AND LOWER(AvailabilityStatus) = 'available'", 
            (selected_room_type,))
        
        if available_rooms:
            for room in available_rooms:
                print(f"RoomID: {room[0]}, Cost: ${room[1]}")
            
            room_id = input("Enter RoomID: ")
            selected_room = next((room for room in available_rooms if str(room[0]) == room_id), None)
            
            if selected_room:
                execute_query(conn, """
                INSERT INTO Bill (PatientID, BillType, Amount, Date, PaymentStatus)
                VALUES (?, 'Room', ?, ?, 'Pending')
                """, (patient_id, selected_room[1], date.today()))
                
                execute_query(conn, "UPDATE Room SET AvailabilityStatus = 'occupied' WHERE RoomID = ?", (room_id,))
                
                print(f"Room {room_id} booked successfully. A bill has been generated.")
            else:
                print("Invalid RoomID.")
        else:
            print("The chosen room type is not available.")
    else:
        print("Invalid choice.")

def buy_medicines(conn, patient_id):
    cart = []
    while True:
        print("1. View all Medicines")
        print("2. Search by MedicineID")
        print("3. View Cart")
        print("4. Back")
        choice = input("Enter your option: ")
        
        if choice == '1':
            view_all_medicines(conn, cart)
        elif choice == '2':
            search_medicine(conn, cart)
        elif choice == '3':
            view_cart(conn, patient_id, cart)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

def view_all_medicines(conn, cart):
    cursor = conn.cursor()
    cursor.execute("SELECT MedicineID, Name FROM Medicine")
    medicines = cursor.fetchall()
    for medicine in medicines:
        print(f"MedicineID: {medicine[0]}, Name: {medicine[1]}")
    print("--------------------------------")
    print("1] Search by MedicineID\n2] Back")
    option = input("Enter your option: ")
    if option == '1':
        search_medicine(conn, cart)
    elif option == '2':
        return
    else:
        print("Invalid option. Please enter a number between 1 and 2.")
        view_all_medicines(conn)

def search_medicine(conn, cart):
    medicine_id = input("Enter MedicineID: ")
    cursor = conn.cursor()
    cursor.execute(f"SELECT Name, Cost, Use FROM Medicine WHERE MedicineID='{medicine_id}'")
    medicine = cursor.fetchone()
    if medicine:
        print(f"Name: {medicine[0]}, Cost: {medicine[1]}, Use: {medicine[2]}")
        add_to_cart = input("Add the medicine to the cart [y/n]: ")
        if add_to_cart.lower() == 'y':
            cart.append((medicine_id, medicine[0], medicine[1]))
    else:
        print("Medicine not found.")
    return

def view_cart(conn, patient_id, cart):
    if not cart:
        print("Cart is empty.")
        return
    total_cost = 0
    print("Medicines in cart:")
    for medicine in cart:
        print(f"MedicineID: {medicine[0]}, Name: {medicine[1]}, Cost: {medicine[2]}")
        total_cost += medicine[2]
    print(f"Total Cost: {total_cost}")
    
    pay = input("Do you wish to pay [y/n]: ")
    if pay.lower() == 'y':
        print("You can make the payment in Bills.")
        cursor = conn.cursor()
        medicines_bought = ", ".join([f"{med[1]} (ID: {med[0]})" for med in cart])
        today = datetime.today().strftime('%Y-%m-%d')
        cursor.execute(f"INSERT INTO Bill (PatientID, BillType, Amount, Date, PaymentStatus) VALUES (?, 'Medicines', ?, ?, 'Pending')", 
                       (patient_id, total_cost, today))
        conn.commit()

def execute_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()

def fetch_data(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

def doctors_menu(conn):
    while True:
        print("\nDoctors Menu")
        print("1] View Doctors")
        print("2] Add Doctor")
        print("3] Edit Doctor Profile")
        print("4] Back")
        print("5] Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_doctors(conn)
        elif choice == '2':
            add_doctor(conn)
        elif choice == '3':
            edit_doctor_profile(conn)
        elif choice == '4':
            return
        elif choice == '5':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

def edit_doctor_profile(conn):
    doctor_id = input("Enter Doctor ID to edit: ")
    
    # First check if doctor exists
    doctor = fetch_data(conn, "SELECT * FROM Doctor WHERE DoctorID = ?", (doctor_id,))
    if not doctor:
        print("Doctor not found!")
        return
    
    print("\nEdit Doctor Profile")
    print("1] Name")
    print("2] Date of Birth")
    print("3] Gender")
    print("4] Specialization")
    print("5] Phone Number")
    print("6] Email")
    print("7] Address")
    print("8] Years of Experience")
    print("9] Work Status")
    
    choice = input("Enter field to edit (1-9): ")
    
    field_mapping = {
        '1': ('Name', 'TEXT'),
        '2': ('DOB', 'DATE (YYYY-MM-DD)'),
        '3': ('Gender', 'TEXT'),
        '4': ('Specialization', 'TEXT'),
        '5': ('PhoneNo', 'TEXT'),
        '6': ('EmailID', 'TEXT'),
        '7': ('Address', 'TEXT'),
        '8': ('YearsOfExperience', 'INTEGER'),
        '9': ('WorkStatus', 'TEXT')
    }
    
    if choice in field_mapping:
        field, data_type = field_mapping[choice]
        new_value = input(f"Enter new {field} ({data_type}): ")
        
        # Convert to integer if years of experience
        if field == 'YearsOfExperience':
            try:
                new_value = int(new_value)
            except ValueError:
                print("Invalid input. Years of experience must be a number.")
                return
        
        # Update the database
        execute_query(conn, f"UPDATE Doctor SET {field} = ? WHERE DoctorID = ?", 
                     (new_value, doctor_id))
        print(f"Doctor {field} updated successfully.")
    else:
        print("Invalid choice!")
    input("\nPress Enter to continue...")

def patients_menu(conn):
    while True:
        print("\nPatients Menu")
        print("1] View Patients")
        print("2] Add Patient")
        print("3] Edit Patient Profile")
        print("4] Back")
        print("5] Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_patients(conn)
        elif choice == '2':
            add_patient(conn)
        elif choice == '3':
            edit_patient_profile(conn)
        elif choice == '4':
            return
        elif choice == '5':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

def add_doctor(conn):
    password = input("Enter Password: ")

    execute_query(conn, "INSERT INTO LoginCredits (Password, UserType) VALUES (?, ?)", (password, 'Doctor'))

    cursor = conn.cursor()
    cursor.execute("SELECT last_insert_rowid()")
    user_id = cursor.fetchone()[0]

    print(f"Doctor UserID is: {user_id}")
    name = input("Doctor Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    gender = input("Gender: ")
    specialization = input("Specialization: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    experience = int(input("Years of Experience: "))
    execute_query(conn, """
    INSERT INTO Doctor (Name, DOB, Gender, Specialization, PhoneNo, EmailID, Address, YearsOfExperience, WorkStatus)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, dob, gender, specialization, phone, email, address, experience, 'Active'))
    print(f"Doctor {name} added successfully.")
    input("\nPress Enter to continue...")

def add_patient(conn):
    password = input("Enter Password for Patient: ")
    
    # Add login credentials
    execute_query(conn, "INSERT INTO LoginCredits (Password, UserType) VALUES (?, ?)", (password, 'Patient'))
    
    cursor = conn.cursor()
    cursor.execute("SELECT last_insert_rowid()")
    user_id = cursor.fetchone()[0]
    
    print(f"Patient UserID is: {user_id}")
    
    # Get patient details
    name = input("Patient Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    weight = float(input("Weight (in kg): "))
    height = float(input("Height (in cm): "))
    gender = input("Gender: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    medical_history = input("Medical History (if any): ")
    
    # Insert patient data
    execute_query(conn, """
    INSERT INTO Patient (Name, DOB, Weight, Height, Gender, PhoneNo, EmailID, Address, MedicalHistory)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, dob, weight, height, gender, phone, email, address, medical_history))
    
    print(f"Patient {name} added successfully.")
    input("\nPress Enter to continue...")

def edit_patient_profile(conn):
    patient_id = input("Enter Patient ID to edit: ")
    
    # First check if patient exists
    patient = fetch_data(conn, "SELECT * FROM Patient WHERE PatientID = ?", (patient_id,))
    if not patient:
        print("Patient not found!")
        return
    
    print("\nEdit Patient Profile")
    print("1] Name")
    print("2] Date of Birth")
    print("3] Weight")
    print("4] Height")
    print("5] Gender")
    print("6] Phone Number")
    print("7] Email")
    print("8] Address")
    print("9] Medical History")
    
    choice = input("Enter field to edit (1-9): ")
    
    field_mapping = {
        '1': ('Name', 'TEXT'),
        '2': ('DOB', 'DATE (YYYY-MM-DD)'),
        '3': ('Weight', 'REAL (in kg)'),
        '4': ('Height', 'REAL (in cm)'),
        '5': ('Gender', 'TEXT'),
        '6': ('PhoneNo', 'TEXT'),
        '7': ('EmailID', 'TEXT'),
        '8': ('Address', 'TEXT'),
        '9': ('MedicalHistory', 'TEXT')
    }
    
    if choice in field_mapping:
        field, data_type = field_mapping[choice]
        new_value = input(f"Enter new {field} ({data_type}): ")
        
        # Convert to float if weight or height
        if field in ['Weight', 'Height']:
            try:
                new_value = float(new_value)
            except ValueError:
                print(f"Invalid input. {field} must be a number.")
                return
        
        # Update the database
        execute_query(conn, f"UPDATE Patient SET {field} = ? WHERE PatientID = ?", 
                     (new_value, patient_id))
        print(f"Patient {field} updated successfully.")
    else:
        print("Invalid choice!")
    input("\nPress Enter to continue...")

def add_admin(conn):
    name = input("Admin Name: ")
    password = input("Admin Password: ")
    execute_query(conn, "INSERT INTO LoginCredits (Password) VALUES (?)", (password,))
    print(f"Admin {name} added successfully.")
    input("\nPress Enter to continue...")

def leave_menu(conn):
    while True:
        print("\nLeave Management Menu")
        print("1] See All Leaves")
        print("2] Pending Leaves")
        print("3] Back")
        print("4] Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_all_leaves(conn)
        elif choice == '2':
            handle_pending_leaves(conn)
        elif choice == '3':
            return
        elif choice == '4':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

def view_all_leaves(conn):
    # Fetch all leaves with doctor names
    leaves = fetch_data(conn, """
        SELECT Leave.LeaveID, Doctor.Name, Leave.SelectDate, Leave.ReturnDate, 
               Leave.NoOfDays, Leave.Reason, Leave.LeaveStatus
        FROM Leave
        JOIN Doctor ON Leave.DoctorID = Doctor.DoctorID
        ORDER BY Leave.SelectDate DESC
    """)
    
    if leaves:
        print("\nAll Leaves Information:")
        print("-" * 100)
        print(f"{'LeaveID':^8} | {'Doctor Name':^20} | {'Start Date':^12} | {'End Date':^12} | "
              f"{'Days':^6} | {'Reason':^25} | {'Status':^10}")
        print("-" * 100)
        
        for leave in leaves:
            print(f"{leave[0]:^8} | {leave[1]:^20} | {leave[2]:^12} | {leave[3]:^12} | "
                  f"{leave[4]:^6} | {leave[5]:^10} | {leave[6][:25]:^25}")
        print("-" * 100)
    else:
        print("No leaves found in the system.")
    
    input("\nPress Enter to continue...")

def handle_pending_leaves(conn):
    while True:
        # Fetch pending leaves with doctor names
        pending_leaves = fetch_data(conn, """
            SELECT Leave.LeaveID, Doctor.Name, Leave.SelectDate, Leave.ReturnDate, 
                   Leave.NoOfDays, Leave.Reason
            FROM Leave
            JOIN Doctor ON Leave.DoctorID = Doctor.DoctorID
            WHERE Leave.LeaveStatus = 'Pending'
            ORDER BY Leave.SelectDate
        """)
        
        if pending_leaves:
            print("\nPending Leaves:")
            print("-" * 100)
            print(f"{'LeaveID':^8} | {'Doctor Name':^20} | {'Start Date':^12} | {'End Date':^12} | "
                  f"{'Days':^6} | {'Reason':^25}")
            print("-" * 100)
            
            for leave in pending_leaves:
                print(f"{leave[0]:^8} | {leave[1]:^20} | {leave[2]:^12} | {leave[3]:^12} | "
                      f"{leave[4]:^6} | {leave[5][:25]:^25}")
            print("-" * 100)
            
            print("\n1] Accept Leave")
            print("2] Reject Leave")
            print("3] Back")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                accept_leave(conn)
            elif choice == '2':
                reject_leave(conn)
            elif choice == '3':
                return
            else:
                print("Invalid choice, please enter a number between 1 and 3.")
        else:
            print("No pending leaves found.")
            input("\nPress Enter to continue...")
            return

def accept_leave(conn):
    leave_id = input("Enter LeaveID to accept: ")
    
    # Check if leave exists and is pending
    leave_info = fetch_data(conn, """
        SELECT LeaveID, DoctorID, LeaveStatus
        FROM Leave
        WHERE LeaveID = ?
    """, (leave_id,))
    
    if not leave_info:
        print("Leave ID not found!")
        return
    
    if leave_info[0][2] != 'Pending':
        print("This leave is not in pending state!")
        return
    
    # Update leave status and doctor work status
    try:
        # Start a transaction
        conn.execute("BEGIN TRANSACTION")
        
        # Update leave status
        execute_query(conn, """
            UPDATE Leave 
            SET LeaveStatus = 'Accepted' 
            WHERE LeaveID = ?
        """, (leave_id,))
        
        # Update doctor work status
        execute_query(conn, """
            UPDATE Doctor 
            SET WorkStatus = 'On Leave' 
            WHERE DoctorID = ?
        """, (leave_info[0][1],))
        
        # Commit the transaction
        conn.commit()
        print("Leave accepted successfully.")
        
    except Exception as e:
        # Rollback in case of error
        conn.rollback()
        print(f"Error occurred: {e}")
        print("Leave acceptance failed.")

def reject_leave(conn):
    leave_id = input("Enter LeaveID to reject: ")
    
    # Check if leave exists and is pending
    leave_info = fetch_data(conn, """
        SELECT LeaveStatus
        FROM Leave
        WHERE LeaveID = ?
    """, (leave_id,))
    
    if not leave_info:
        print("Leave ID not found!")
        return
    
    if leave_info[0][0] != 'Pending':
        print("This leave is not in pending state!")
        return
    
    # Update leave status
    execute_query(conn, """
        UPDATE Leave 
        SET LeaveStatus = 'Rejected' 
        WHERE LeaveID = ?
    """, (leave_id,))
    
    print("Leave rejected successfully.")

def admin_function(conn, user_id):
    while True:
        print("\nAdmin Function Menu")
        print("1] Doctors")
        print("2] Patients")
        print("3] Leave Management")
        print("4] Pending Bills")
        print("5] View passwords")
        print("6] Edit password")
        print("7] Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            doctors_menu(conn)
        elif choice == '2':
            patients_menu(conn)
        elif choice == '3':
            leave_menu(conn)
        elif choice == '4':
            pending_bills(conn)
        elif choice == '5':
            view_passwords(conn)
        elif choice == '6':
            edit_password(conn, user_id)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 7.")

def pending_bills(conn):
    bills = fetch_data(conn, "SELECT * FROM Bill WHERE PaymentStatus = 'Pending'")
    if bills:
        for bill in bills:
            print(f"BillID: {bill[0]}, PatientID: {bill[1]}, Amount: {bill[3]}, Date: {bill[4]}, Status: {bill[5]}")
    else:
        print("No pending bills.")
    input("\nPress Enter to continue...")

def view_passwords(conn):
    users = fetch_data(conn, "SELECT * FROM LoginCredits")
    if users:
        for user in users:
            print(f"UserID: {user[0]}, Password: {user[1]}, UserType: {user[2]}")
    else:
        print("No accounts found.")
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
