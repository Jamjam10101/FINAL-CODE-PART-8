import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3

def create_employee_info_window(master):
    con = sqlite3.connect("Laboratory8")

    window = master
    window.title("Employee Information")
    window.geometry("1920x1080")

    bg_image = Image.open("C:\\GUI\\blue.jpg")
    bg_image = bg_image.resize((1950, 1100))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    cursor = con.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS emp_tbl (
        Employee_Number TEXT PRIMARY KEY,
        First_Name TEXT,
        Middle_Name TEXT,
        Last_Name TEXT,
        Suffix TEXT,
        Date_of_Birth TEXT,
        Gender TEXT,
        Nationality TEXT,
        Civil_Status TEXT,
        Department_Name TEXT,
        Designation TEXT,
        Dep_Status TEXT,
        Employee_Status TEXT,
        Date TEXT,
        Contact_Number TEXT,
        Email TEXT,
        Social_Media TEXT,
        Social_Media_Account TEXT,
        Address_Line1 TEXT,
        Address_Line2 TEXT,
        City TEXT,
        State TEXT,
        Country TEXT,
        Zip_Code TEXT,
        Picture_Path TEXT
    )
    ''')

    def save_data_entry():
        firstname = first_name_entry.get()
        middlename = middle_name_entry.get()
        surname = suffix_name_entry.get()
        suffix = suffix_name_entry.get()
        dateofbirth = date_combobox.get()
        gender = gender_combobox.get()
        nationality = nationality_combobox.get()
        civilstatus = civil_combobox.get()
        departmentname = department_entry.get()
        designation = designation_entry.get()
        depstatus = dep_status_combobox.get()
        employeestatus = employee_entry.get()
        date = date_combobox1.get()
        employeenumber = employee_number_entry.get()
        contacnumber = contact_entry.get()
        email = email_entry.get()
        socmed = socmed_combobox.get()
        socmed1 = socmed_acc_entry.get()
        address1 = address_line1_entry.get()
        address2 = address_line2_entry.get()
        city = city_entry.get()
        state = state_entry.get()
        country = country_combobox.get()
        zip = zip_entry.get()
        path = path_entry.get()

        save_data_query = '''INSERT INTO emp_tbl (First_Name, Middle_Name, Last_Name, Suffix, Date_of_Birth, Gender, Nationality, Civil_Status, Department_Name, Designation, Dep_Status, Employee_Status, Date, Employee_Number, Contact_Number, Email, Social_Media, Social_Media_Account, Address_Line1, Address_Line2, City, State, Country, Zip_Code, Picture_Path) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        con.execute(save_data_query, (firstname, middlename, surname, suffix, dateofbirth, gender, nationality, civilstatus,
                  departmentname, designation, depstatus, employeestatus, date, employeenumber,
                  contacnumber, email, socmed, socmed1, address1, address2, city, state, country, zip, path))
        con.commit()

        messagebox.showinfo(title="Data Saved", message="Data has been saved to SQL")
        print("\nData saved...........")

    def select_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            load_image(file_path)

    def load_image(file_path):
        image = Image.open(file_path)
        image = image.resize((130, 130))
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

    font_style = ("Times New Roman", 12, "bold")
    font = ("Times New Roman", 12)

    main_frame = tk.Frame(window)
    main_frame.config(bg="light blue")
    main_frame.place(relx=0.25, rely=0.25, anchor="center")

    user_info_frame = tk.LabelFrame(window, text="")
    user_info_frame.place(relx=0.23, rely=0.186, anchor="center")

    user_frame = tk.Frame(user_info_frame)
    user_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    pic_frame = tk.LabelFrame(window, text="")
    pic_frame.place(relx=0.099, rely=0.110, anchor="e")

    pic1_frame = tk.Frame(pic_frame, bg='red')
    pic1_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    dept_info_frame = tk.LabelFrame(window, text="")
    dept_info_frame.place(relx=0.23, rely=0.3438, anchor="center")

    dept_frame = tk.Frame(dept_info_frame)
    dept_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    contact_info_frame = tk.LabelFrame(window, text="Contact Info", font=font_style)
    contact_info_frame.place(relx=0.2309, rely=0.51, anchor="center")

    contact_frame = tk.Frame(contact_info_frame)
    contact_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    address_info_frame = tk.LabelFrame(window, text="Address", font=font_style)
    address_info_frame.place(relx=0.23, rely=0.76, anchor="center")

    address_frame = tk.Frame(address_info_frame)
    address_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    button_frame = tk.Frame(window)
    button_frame.place(relx=0.074, rely=0.95, anchor="center")

    select_image_button = ttk.Button(user_frame, text="Select Image", command=select_image)
    select_image_button.grid(row=1, column=0, padx=37, pady=40, sticky="s")

    user = tk.Frame(user_frame)
    user.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    first_name_label = tk.Label(user, text="First name", font=font_style)
    first_name_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    middle_name_label = tk.Label(user, text="Middle name", font=font_style)
    middle_name_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

    last_name_label = tk.Label(user, text="Last name", font=font_style)
    last_name_label.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    suffix_name_label = tk.Label(user, text="Suffix", font=font_style)
    suffix_name_label.grid(row=1, column=4, padx=5, pady=5, sticky="w")

    first_name_entry = tk.Entry(user, font=font_style, width=20)
    first_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    middle_name_entry = tk.Entry(user, font=font_style, width=20)
    middle_name_entry.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

    last_name_entry = tk.Entry(user, font=font_style, width=20)
    last_name_entry.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

    suffix_name_entry = tk.Entry(user, font=font_style, width=10)
    suffix_name_entry.grid(row=2, column=4, padx=5, pady=5, sticky="ew")

    date_label = tk.Label(user, text="Date of birth", font=font_style)
    date_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    gender_label = tk.Label(user, text="Gender", font=font_style)
    gender_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")

    nationality_label = tk.Label(user, text="Nationality", font=font_style)
    nationality_label.grid(row=3, column=3, padx=5, pady=5, sticky="w")

    civil_label = tk.Label(user, text="Civil status", font=font_style)
    civil_label.grid(row=3, column=4, padx=5, pady=5, sticky="w")

    date_combobox = ttk.Combobox(user, state="readonly", width=5, font=font_style)
    date_combobox.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
    date_options = [f"{str(month).zfill(2)}/{str(day).zfill(2)}/{str(year)[-2:]}" for year in range(2000, 2025) for month in range(1, 12) for day in range(1, 32)]
    date_combobox['values'] = date_options

    gender_combobox = ttk.Combobox(user, state="readonly", width=10, font=font_style)
    gender_combobox.grid(row=4, column=2, padx=5, pady=5, sticky="ew")
    gender_combobox['values'] = ("Male", "Female", "Other")

    nationality_combobox = ttk.Combobox(user, state="readonly", width=20, font=font_style)
    nationality_combobox.grid(row=4, column=3, padx=5, pady=5, sticky="ew")
    nationality_combobox['values'] = ("Filipino", "Japanese", "American", "Other")

    civil_combobox = ttk.Combobox(user, state="readonly", width=10, font=font_style)
    civil_combobox.grid(row=4, column=4, padx=5, pady=5, sticky="ew")
    civil_combobox['values'] = ("married", "widow", "single", "UMAI")

    dept = tk.Frame(dept_frame)
    dept.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    department_label = tk.Label(dept, text="Department Name", font=font_style)
    department_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    designation_label = tk.Label(dept, text="Designation", font=font_style)
    designation_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    dep_status_label = ttk.Label(dept, text="Qualities Dep Status", font=font_style)
    dep_status_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    employee_label = tk.Label(dept, text="Employee Status", font=font_style)
    employee_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    date_label = ttk.Label(dept, text="Date", font=font_style)
    date_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    employee_number_label = tk.Label(dept, text="Employee Number", font=font_style)
    employee_number_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")

    department_entry = tk.Entry(dept, font=font_style, width=48)
    department_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    designation_entry = tk.Entry(dept, font=font_style, width=25)
    designation_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    dep_status_combobox = ttk.Combobox(dept, font=font_style, state="readonly", width=20)
    dep_status_combobox.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
    dep_status_combobox['values'] = ("A", "B", "C", "D")

    employee_entry = tk.Entry(dept, font=font_style, width=10)
    employee_entry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

    date_combobox1 = ttk.Combobox(dept, state="readonly", width=5, font=font_style)
    date_combobox1.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
    date_options = [f"{str(month).zfill(2)}/{str(day).zfill(2)}/{str(year)[-2:]}" for year in range(2024, 2025) for month in range(1, 12) for day in range(1, 32)]
    date_combobox1['values'] = date_options

    employee_number_entry = tk.Entry(dept, font=font_style, width=10)
    employee_number_entry.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

    cont = tk.Frame(contact_frame)
    cont.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    contact_label = tk.Label(cont, text="Contact No.", font=font_style)
    contact_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    email_label = tk.Label(cont, text="Email", font=font_style)
    email_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    socmed_label = tk.Label(cont, text="Social Media", font=font_style)
    socmed_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    socmed_acc_label = tk.Label(cont, text="social media account ID", font=font_style)
    socmed_acc_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    contact_entry = tk.Entry(cont, font=font_style, width=45)
    contact_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    email_entry = tk.Entry(cont, font=font_style, width=52)
    email_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    socmed_combobox = ttk.Combobox(cont, state="readonly", width=10, font=font_style)
    socmed_combobox.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
    socmed_combobox['values'] = ("facebook", "instagram", "twitter", "other")

    socmed_acc_entry = tk.Entry(cont, font=font_style, width=52)
    socmed_acc_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    address_line1 = tk.Label(address_frame, text="address line 1 ", font=font_style)
    address_line1.grid(row=0, column=0, padx=5, pady=5, sticky='w')

    address_line2 = tk.Label(address_frame, text="address line 2 ", font=font_style)
    address_line2.grid(row=3, column=0, padx=5, pady=0, sticky='w')

    address_line1_entry = tk.Entry(address_frame, font=font_style, width=100)
    address_line1_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    address_line2_entry = tk.Entry(address_frame, font=font_style, width=100)
    address_line2_entry.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    user_frame2 = tk.Frame(address_info_frame)
    user_frame2.grid(row=1, column=0, padx=5, pady=5, sticky="nw")

    city_label = tk.Label(user_frame2, text="city/municipality", font=font_style)
    city_label.grid(row=5, column=0, padx=5, pady=2, sticky="w")

    state_label = tk.Label(user_frame2, text="state/province", font=font_style)
    state_label.grid(row=5, column=1, padx=5, pady=2, sticky="w")

    country_label = tk.Label(user_frame2, text="country", font=font_style)
    country_label.grid(row=7, column=0, padx=5, pady=2, sticky="w")

    zip_label = tk.Label(user_frame2, text="zip code", font=font_style)
    zip_label.grid(row=7, column=1, padx=5, pady=2, sticky="w")

    path_label = tk.Label(user_frame2, text="picture path", font=font_style)
    path_label.grid(row=9, column=0, padx=5, pady=2, sticky='w')

    city_entry = tk.Entry(user_frame2, font=font_style, width=67)
    city_entry.grid(row=6, column=0, padx=5, pady=2, sticky="w")

    state_entry = tk.Entry(user_frame2, font=font_style, width=30)
    state_entry.grid(row=6, column=1, padx=5, pady=2, sticky="w")

    country_combobox = ttk.Combobox(user_frame2, state="readonly", width=65, font=font_style)
    country_combobox.grid(row=8, column=0, padx=5, pady=2, sticky="w")
    country_combobox['values'] = ("japan","Philippines", "Russia", "America", "Spain")

    zip_entry = tk.Entry(user_frame2, font=font_style, width=10)
    zip_entry.grid(row=8, column=1, padx=5, pady=2, sticky="w")

    path_entry = tk.Entry(user_frame2, font=font_style, width=99)
    path_entry.grid(row=10, column=0, columnspan=2, padx=5, pady=2, sticky="w")

    default_image = Image.open("C:\\GUI\\defaultphoto.jpg")
    default_image = default_image.resize((130, 130))
    default_photo = ImageTk.PhotoImage(default_image)
    image_label = tk.Label(pic1_frame, image=default_photo)
    image_label.grid(row=0, column=0, sticky="w")

    def cancel():
        exit()

#blue
    save_button = tk.Button(button_frame, text="Save", width=10, font=("Times New Roman", 12), bg="red", fg='white', cursor="hand2", command=save_data_entry)
    save_button.grid(row=22, column=0, padx=5, pady=5, sticky="w")

    cancel_button = tk.Button(button_frame, text="Cancel", width=10, font=("Times New Roman", 12), cursor="hand2", command=cancel)
    cancel_button.grid(row=22, column=1, padx=5, pady=5, sticky="w")

    window.mainloop()

def EmployeeInfo(master):
    create_employee_info_window(master)