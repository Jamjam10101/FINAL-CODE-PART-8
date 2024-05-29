import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import USERINFO
import PAYROLL
import EMPINFO

def admin(master):
    window = master
    window.title("ADMIN")
    window.geometry("1920x1080")

    bg_image = Image.open("C:\\GUI\\adamson.jpg")
    bg_image = bg_image.resize((1950, 1100))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    main_frame = tk.Frame(window)
    main_frame.place(relx=0.25, rely=0.50, anchor="center")


    def open_employee_info(self):
        self.master.withdraw()  # Hide the login window
        employee_info_window = tk.Toplevel(self.master)
        EMPINFO.EmployeeInfo(employee_info_window)


    def open_payroll(self):
        self.master.withdraw()  # Hide the login window
        payroll_window = tk.Toplevel(self.master)
        PAYROLL.Payroll(payroll_window)


    def open_user(self):
        self.master.withdraw()  # Hide the login window
        user_window = tk.Toplevel(self.master)
        USERINFO.User(user_window)

    update_button = ttk.Button(main_frame, text="emp", command= open_employee_info())
    update_button.grid(row=0, column=0, padx=5, pady=5)

    delete_button = ttk.Button(main_frame, text="user", command=open_payroll())
    delete_button.grid(row=0, column=1, padx=5, pady=5)

    cancel_button = ttk.Button(main_frame, text="payroll", command=open_user())
    cancel_button.grid(row=0, column=2, padx=5, pady=5)

    window.mainloop()

def Admin(master):
    admin(master)