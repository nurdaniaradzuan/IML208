from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import os

#THE FULL PATH OF THE FILE
file_path = os.path.join(os.path.dirname(__file__), "counselling_data.txt")

# FORM DETAILS
root = Tk()
root.title('New Patient Registration Form')
root.geometry('1000x500+200+100')
root.configure(bg="#fff")
root.resizable(False, False)

# Load Image
image_path = "C:/Users/User/OneDrive/Pictures/woopyy.png"
img = PhotoImage(file=image_path)

# Display Image
image_label = Label(root, image=img, bg="#fff")
image_label.place(x=20, y=20)

# Main Frame
frame = Frame(root, width=350, height=400, bg="white")
frame.place(x=480, y=70)

# Heading
heading = Label(frame, text='FULLSUN COUNSELLING', fg='#ff9248', bg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
heading.place(x=20, y=1)

# VARIABLE 1: PATIENT NAME
def on_enter(e):
    patient_name.delete(0, 'end')

def on_leave(e):
    name = patient_name.get()
    if name == '':
        patient_name.insert(0, 'PATIENT NAME')
    else:
        patient_name.delete(0, 'end')
        patient_name.insert(0, name.upper())

patient_name = Entry(frame, width=25, fg='black', border=0, bg='white', font=('arial', 12))
patient_name.insert(0, 'PATIENT NAME')
patient_name.place(x=30, y=50)
patient_name.bind('<FocusIn>', on_enter)
patient_name.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=30, y=80)

# VARIABLE 2: PATIENT AGE
patient_age = [str(i) for i in range(13, 18)]
list_of_ages = StringVar()
patient_age = ttk.Combobox(frame, textvariable=list_of_ages, values=patient_age, state='readonly', width=30, font=('arial', 13))
patient_age.place(x=30, y=100)
patient_age.set('SELECT YOUR AGE')

# VARIABLE 3: PATIENT PHONE NUMBER
def on_enter(e):
    patient_phoneno.delete(0, 'end')

def on_leave(e):
    number = patient_phoneno.get()
    if number == '':
        patient_phoneno.insert(0, 'PHONE NUMBER')

patient_phoneno = Entry(frame, width=25, fg='black', border=0, bg='white', font=('arial', 12))
patient_phoneno.insert(0, 'PHONE NUMBER')
patient_phoneno.place(x=30, y=150)
patient_phoneno.bind('<FocusIn>', on_enter)
patient_phoneno.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=30, y=180)

# VARIABLE 4: TIME BOOKING FOR A SESSION
def on_enter_time(e):
    time_booking.delete(0, 'end')

def on_leave_time(e):
    time = time_booking.get()
    if time == '':
        time_booking.insert(0, 'SESSION TIME (00:00 AM/PM)')

time_booking = Entry(frame, width=25, fg='black', border=0, bg='white', font=('arial', 12))
time_booking.insert(0, 'SESSION TIME (12:00 AM/PM)')
time_booking.place(x=30, y=200)
time_booking.bind('<FocusIn>', on_enter_time)
time_booking.bind('<FocusOut>', on_leave_time)

Frame(frame, width=295, height=2, bg='black').place(x=30, y=230)

# VARIABLE 5: DATE BOOKING FOR A SESSION
def on_date_select():
    selected_date = date_booking.get_date()
    print(f"Selected Date: {selected_date}")

date_label = Label(frame, text='SESSION DATE', fg='black', bg='white', font=('arial', 12))
date_label.place(x=31, y=250)

date_booking = DateEntry(frame, width=12, background='white', fg='black', border=0, font=('arial', 12), date_pattern='dd/MM/yyyy')
date_booking.set_date('01/01/2023') 
date_booking.place(x=35, y=280)
date_booking.bind('<FocusOut>', on_date_select)

# PHONE NUMBER FORMAT
def format_phone_number(phone_number):
    formatted_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
    return formatted_number

# SAVING PATIENTS DATA INTO THE FILE (patient_booking_data.txt)
def save_booking_data_to_file(data):
    with open("counselling_data.txt", "a") as file:
        file.write(data + "\n")

# BOOKING BUTTON COMMAND
def book_button_click():
    try:
        patient_name_value = patient_name.get()
        patient_age_value = patient_age.get()
        patient_phoneno_value = patient_phoneno.get()
        time_booking_value = time_booking.get()
        date_booking_value = date_booking.get()

        #VALIDATE INPUT DATA
        if not patient_name_value or not patient_age_value or not patient_phoneno_value or not time_booking_value or not date_booking_value:
            raise ValueError("All fields must be filled")

        #AGE
        int(patient_age_value)

        #PHONE NUMBER (Either 10 or 11 digits)
        if not patient_phoneno_value.isdigit() or not (len(patient_phoneno_value) == 10 or len(patient_phoneno_value) == 11):
            raise ValueError("Invalid phone number format. Please enter either 10 or 11 digits.")

        formatted_phone_number = format_phone_number(patient_phoneno_value)

        booking_info = f"Name: {patient_name_value}\nAge: {patient_age_value}\nPhone Number: {formatted_phone_number}\n" \
                        f"Time: {time_booking_value}\nDate: {date_booking_value}"
        
        # Convert time to 24-hour format
        time_obj = datetime.strptime(time_booking_value, '%I:%M %p')
        time_booking_value_24h = time_obj.strftime('%H:%M')

        booking_info = f"Name: {patient_name_value}\nAge: {patient_age_value}\nPhone Number: {formatted_phone_number}\n" \
                        f"Time: {time_booking_value_24h}\nDate: {date_booking_value}"

        # Display success message
        messagebox.showinfo("Booking Success", "Booking has been successful!\n\n" + booking_info)

        # SAVE DATA
        save_booking_data_to_file(booking_info)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# DELETE THE DATA
def delete_patient_data(patient_name_to_delete):
    with open("counselling_data.txt", "r") as file:
        lines = file.readlines()

    new_lines = [line for line in lines if f"Name: {patient_name_to_delete}" not in line]

    with open("counselling_data.txt", "w") as file:
        file.writelines(new_lines)

# EXAMPLE
delete_patient_data('ZUZU')

#BUTTON FOR BOOKING (ADD DATA)
Button(frame, width=40, pady=8, text='BOOK!', bg='#ff9248', fg='white', border=0, command=book_button_click).place(x=35, y=330)

root.mainloop()