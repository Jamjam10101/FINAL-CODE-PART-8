import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3

def create_user_info_window(master):
    conn = sqlite3.connect('Laboratory8')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS user_account (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        suffix TEXT,
        department TEXT,
        designation TEXT,
        username TEXT,
        password TEXT,
        confirm_password TEXT,
        user_type TEXT,
        user_status TEXT,
        employee_number TEXT
    )
    ''')
    conn.commit()

    def submit_button():
        first_name = first_name_entry.get()
        middle_name = middle_name_entry.get()
        last_name = last_name_entry.get()
        suffix = suffix_name_entry.get()
        department = department_entry.get()
        designation = designation_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        user_type = user_type_entry.get()
        user_status = user_status_entry.get()
        employee_number = employee_number_entry.get()

        c.execute('''
        INSERT INTO user_account (
            first_name, middle_name, last_name, suffix, department, designation,
            username, password, confirm_password, user_type, user_status, employee_number
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, middle_name, last_name, suffix, department, designation, username, password, confirm_password,
              user_type, user_status, employee_number))

        conn.commit()
        messagebox.showwarning(title="Data Saved", message="Data has been saved to SQL")
        print("\nData saved...........")
        print("Submit button clicked!")

    def cancel_button():
        print("Cancel button clicked!")
        window.destroy()

    def select_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            load_image(file_path)

    def load_image(file_path):
        image = Image.open(file_path)
        image = image.resize((150, 150))
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

    window = master
    window.title("User Account Information")
    window.geometry("1920x1080")

    bg_image = Image.open("C:\\GUI\\blue.jpg")
    bg_image = bg_image.resize((1950, 1100))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    font_style1 = ("Times New Roman", 35, "bold")
    font_style = ("Times New Roman", 12, "bold")
    font = ("Times New Roman", 12)

    main_frame = tk.Frame(window)
    main_frame.place(relx=0.25, rely=0.50, anchor="center")

#user acc
    employee_label = tk.Label(window, text="USER ACCOUNT INFORMATION", font=font_style1)
    employee_label.place(relx=0.54, rely=0.30, anchor="center")

    user_info_frame = tk.LabelFrame(window, text="")
    user_info_frame.place(relx=0.5, rely=0.5, anchor="center")

    user_frame = tk.Frame(user_info_frame)
    user_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    user_frame2 = tk.Frame(user_info_frame)
    user_frame2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    user_frame3 = tk.Frame(user_info_frame)
    user_frame3.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    pic_frame = tk.LabelFrame(window, text="")
    pic_frame.place(relx=0.345, rely=0.39, anchor="e")

    pic1_frame = tk.Frame(pic_frame)
    pic1_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    user = tk.Frame(user_frame)
    user.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    user2 = tk.Frame(user_frame2)
    user2.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    user3 = tk.Frame(user_frame3)
    user3.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    select_image_button = ttk.Button(user, text="Select Image", command=select_image)
    select_image_button.grid(row=1, column=0, padx=55, pady=20, sticky="s")

    first_name_label = tk.Label(user, text="First name", font=font_style)
    first_name_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    middle_name_label = tk.Label(user, text="Middle name", font=font_style)
    middle_name_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

    last_name_label = tk.Label(user, text="Last name", font=font_style)
    last_name_label.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    suffix_name_label = tk.Label(user, text="Suffix", font=font_style)
    suffix_name_label.grid(row=1, column=4, padx=5, pady=5, sticky="w")

    department_label = tk.Label(user, text="Department", font=font_style)
    department_label.grid(row=1, column=5, padx=5, pady=5, sticky="w")

    first_name_entry = tk.Entry(user, font=font_style, width=17, bg='light blue')
    first_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    middle_name_entry = tk.Entry(user, font=font_style, width=17, bg='light blue')
    middle_name_entry.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

    last_name_entry = tk.Entry(user, font=font_style, width=17, bg='light blue')
    last_name_entry.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

    suffix_name_entry = tk.Entry(user, font=font_style, width=15, bg='light blue')
    suffix_name_entry.grid(row=2, column=4, padx=5, pady=5, sticky="ew")

    department_entry = tk.Entry(user, font=font_style, width=17, bg='light blue')
    department_entry.grid(row=2, column=5, padx=5, pady=5, sticky="ew")

    designation_label = tk.Label(user2, text="Designation", font=font_style)
    designation_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    username_label = tk.Label(user2, text="Username", font=font_style)
    username_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    password_label = tk.Label(user2, text="Password", font=font_style)
    password_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    confirm_password_label = tk.Label(user3, text="Confirm Password", font=font_style)
    confirm_password_label.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    user_type_label = tk.Label(user3, text="User Type", font=font_style)
    user_type_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")

    user_status_label = tk.Label(user3, text="User Status", font=font_style)
    user_status_label.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    employee_number_label = tk.Label(user3, text="Employee Number", font=font_style)
    employee_number_label.grid(row=0, column=6, padx=5, pady=5, sticky="w")

    designation_entry = tk.Entry(user2, font=font_style, width=35, bg='light blue')
    designation_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    username_entry = tk.Entry(user2, font=font_style, width=35)
    username_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    password_entry = tk.Entry(user2, font=font_style, width=35)
    password_entry.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

    confirm_password_entry = tk.Entry(user3, font=font_style, width=27)
    confirm_password_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

    user_type_entry = tk.Entry(user3, font=font_style, width=27)
    user_type_entry.grid(row=1, column=4, padx=5, pady=5, sticky="ew")

    user_status_entry = tk.Entry(user3, font=font_style, width=27)
    user_status_entry.grid(row=1, column=5, padx=5, pady=5, sticky="ew")

    employee_number_entry = tk.Entry(user3, font=font_style, width=27)
    employee_number_entry.grid(row=1, column=6, padx=5, pady=5, sticky="ew")

    buttons_frame = tk.Frame(user_info_frame)
    buttons_frame.grid(row=4, column=0, padx=5, pady=5, sticky="e")

    update_button = ttk.Button(buttons_frame, text="Update", command=submit_button)
    update_button.grid(row=0, column=0, padx=5, pady=5)

    delete_button = ttk.Button(buttons_frame, text="Delete")
    delete_button.grid(row=0, column=1, padx=5, pady=5)

    cancel_button = ttk.Button(buttons_frame, text="Cancel", command=cancel_button)
    cancel_button.grid(row=0, column=2, padx=5, pady=5)

    default_image_path = "C:\\GUI\\defaultphoto.jpg"
    default_image = Image.open(default_image_path)
    default_image = default_image.resize((130, 130))
    default_photo = ImageTk.PhotoImage(default_image)
    image_label = tk.Label(pic1_frame, image=default_photo)
    image_label.grid(row=0, column=0, sticky="w")

    window.mainloop()
    conn.close()

def User(master):
    create_user_info_window(master)
