import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import USERINFO
import PAYROLL
import EMPINFO

#hello po 



class LoginSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Login System")
        self.master.configure(bg="light blue")
        self.master.geometry("700x600")
        self.frame = tk.Frame(master=self.master, bg="light blue")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")  # Placing the frame in the center

        self.create_widgets()

    def create_widgets(self):
        self.create_label()
        self.create_entry_username()
        self.create_entry_password()
        self.create_button_login()
        self.create_checkbox_remember()

    def create_label(self):
        self.label = tk.Label(
            master=self.frame, text="Login System", font=("Times New Roman bold", 50), bg="light blue", fg="black"
        )
        self.label.grid(row=0, column=0, columnspan=2, pady=20)

    def create_entry_username(self):
        self.username = tk.StringVar()
        tk.Label(self.frame, text="Username:", font=("Times New Roman", 18), bg="light blue", fg="black").grid(row=1, column=0, sticky="e")
        self.entry_username = tk.Entry(
            master=self.frame, textvariable=self.username, width=30, font=("Times New Roman", 18)
        )
        self.entry_username.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    def create_entry_password(self):
        self.password = tk.StringVar()
        tk.Label(self.frame, text="Password:", font=("Times New Roman", 18), bg="light blue", fg="black").grid(row=2, column=0, sticky="e")
        self.entry_password = tk.Entry(
            master=self.frame,
            textvariable=self.password,
            width=30,
            font=("Times New Roman", 18),
            show="*",
        )
        self.entry_password.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    def create_button_login(self):
        self.button = tk.Button(master=self.frame, text="Login", command=self.handle_login, font=("Arial", 18))
        self.button.grid(row=3, column=1, pady=20)

    def create_checkbox_remember(self):
        self.remember_me = tk.BooleanVar()
        self.checkbox_remember_me = tk.Checkbutton(
            master=self.frame, text="Remember Me", variable=self.remember_me, font=("Times New Roman", 18), bg="light blue", fg="black"
        )
        self.checkbox_remember_me.grid(row=4, column=1, pady=10)

    def handle_login(self):
        username = self.username.get()
        password = self.password.get()

        if not username:
            messagebox.showwarning("Login Failed", "Please enter a username.")
            return

        if not password:
            messagebox.showwarning("Login Failed", "Please enter a password.")
            return

        # Define credentials for employee info and payroll systems
        employee_info_credentials = {'username': '2', 'password': '2'}
        payroll_credentials = {'username': '1', 'password': '1'}
        user_credentials = {'username': '3', 'password': '3'}
        admin_credentials = {'username': 'admin', 'password': 'admin'}

        if username == employee_info_credentials['username'] and password == employee_info_credentials['password']:
            self.open_employee_info()
        elif username == payroll_credentials['username'] and password == payroll_credentials['password']:
            self.open_payroll()
        elif username == user_credentials['username'] and password == user_credentials['password']:
            self.open_user()
        elif username == admin_credentials['username'] and password == admin_credentials['password']:
            self.admin()
        else:
            messagebox.showwarning("Login Failed", "Invalid username or password.")

    def open_employee_info(self):
        self.master.withdraw()  # Hide the login window
        employee_info_window = tk.Toplevel(self.master)
        EMPINFO.EmployeeInfo(employee_info_window)

    def open_payroll(self):
        self.master.withdraw()  # Hide the login window
        payroll_window = tk.Toplevel(self.master)
        PAYROLL.Payroll(payroll_window)

    def open_user(self):
        self.master.withdraw()
        user_window = tk.Toplevel(self.master)
        USERINFO.User(user_window)

    def admin(self):
        self.master.withdraw()
        admin = tk.Toplevel(self.master)
        self.admin_window(admin)

    def logout(self):
        self.master.destroy()

        root = tk.Tk()
        app = LoginSystem(root)
        root.mainloop()

    def admin_window(self, window):
        window.title("ADMIN")
        window.geometry("1920x1080")

        bg_image = Image.open("C:\\GUI\\bg.jpg")
        bg_image = bg_image.resize((1950, 1100))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(window, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)



        emp_button = ttk.Button(window, text="Employee Personal Information", command=self.open_employee_info)
        emp_button.place(relx=.50, rely=0.05)

        payroll_button = ttk.Button(window, text="Payroll", command=self.open_payroll)
        payroll_button.place(relx=0.38, rely=0.05)

        uai_button = ttk.Button(window, text="User Account Information", command=self.open_user)
        uai_button.place(relx=0.42, rely=0.05)

        logout_button = ttk.Button(window, text="Logout", command=self.logout)
        logout_button.place(relx=0.90, rely=0.90)

        def payroll_data():
            # Connect to SQLite database
            conn = sqlite3.connect('Laboratory8')
            cursor = conn.cursor()

            # Execute the query to fetch data
            cursor.execute("SELECT * FROM Payroll")
            records = cursor.fetchall()

            # Close the database connection
            conn.close()

            # Clear the previous contents of the Treeview
            for row in payroll_tree.get_children():
                payroll_tree.delete(row)

            # Insert new data into the Treeview
            for record in records:
                payroll_tree.insert("", "end", values=record)

        def emp_data():
            # Connect to SQLite database
            conn = sqlite3.connect('Laboratory8')
            cursor = conn.cursor()

            # Execute the query to fetch data
            cursor.execute("SELECT * FROM emp_tbl")
            records = cursor.fetchall()

            # Close the database connection
            conn.close()

            # Clear the previous contents of the Treeview
            for row in emp_tree.get_children():
                emp_tree.delete(row)

            # Insert new data into the Treeview
            for record in records:
                emp_tree.insert("", "end", values=record)

        def user_data():
            # Connect to SQLite database
            conn = sqlite3.connect('Laboratory8')
            cursor = conn.cursor()

            # Execute the query to fetch data
            cursor.execute("SELECT * FROM user_account")
            records = cursor.fetchall()

            # Close the database connection
            conn.close()

            # Clear the previous contents of the Treeview
            for row in user_tree.get_children():
                user_tree.delete(row)

            # Insert new data into the Treeview
            for record in records:
                user_tree.insert("", "end", values=record)

        # Create a frame for the buttons
        button_frame = Frame(window)
        button_frame.pack(pady=20)

        # Add buttons to fetch and display data for each table
        fetch_payroll_button = Button(button_frame, text="Payroll Data", command=payroll_data)
        fetch_payroll_button.pack(side=LEFT, padx=10)

        fetch_emp_button = Button(button_frame, text="Employee Data", command=emp_data)
        fetch_emp_button.pack(side=LEFT, padx=10)

        fetch_user_button = Button(button_frame, text="User Data", command=user_data)
        fetch_user_button.pack(side=LEFT, padx=10)

        # Create a frame for the payroll Treeview and scrollbar
        payroll_frame = Frame(window)
        payroll_frame.pack(pady=20)

        # Add a horizontal scrollbar to the payroll frame
        payroll_scrollbar = Scrollbar(payroll_frame, orient=HORIZONTAL)
        payroll_scrollbar.pack(side=BOTTOM, fill=X)

        # Create a Treeview to display payroll data in a table format
        payroll_tree = ttk.Treeview(payroll_frame, columns=(
        "Employee_Number", "Department", "Rate_1", "Hour_1", "Income_1", "Rate_2", "Hour_2", "Income_2", "Rate_3",
        "Hour_3",
        "Income_3", "Gross_income", "Net_income", "First_name", "Middle_name", "Surname", "Civil_Status",
        "Qualified_Dependent_Status", "Pay_Date", "Employee_Status",
        "Designation", "SSS_Contribution", "Phil_Health_Contribution", "Pag_Ibig_Contribution",
        "Income_Tax_Contribution", "SSS_Loan", "Pag_Ibig_Loan",
        "Faculty_Save_Deposit", "Faculty_Saving_Loan", "Salary_Loan", "Other_Loans", "Total_Deduction"),
                                    show='headings', xscrollcommand=payroll_scrollbar.set)

        # Configure the scrollbar for payroll Treeview
        payroll_scrollbar.config(command=payroll_tree.xview)

        # Define headings for payroll Treeview
        payroll_tree.heading("Employee_Number", text="Employee Number")
        payroll_tree.heading("Department", text="Department")
        payroll_tree.heading("Rate_1", text="Rate 1")
        payroll_tree.heading("Hour_1", text="Hour 1")
        payroll_tree.heading("Income_1", text="Income 1")
        payroll_tree.heading("Rate_2", text="Rate 2")
        payroll_tree.heading("Hour_2", text="Hour 2")
        payroll_tree.heading("Income_2", text="Income 2")
        payroll_tree.heading("Rate_3", text="Rate 3")
        payroll_tree.heading("Hour_3", text="Hour 3")
        payroll_tree.heading("Income_3", text="Income 3")
        payroll_tree.heading("Gross_income", text="Gross income")
        payroll_tree.heading("Net_income", text="Net income")
        payroll_tree.heading("First_name", text="First name")
        payroll_tree.heading("Middle_name", text="Middle name")
        payroll_tree.heading("Surname", text="Surname")
        payroll_tree.heading("Civil_Status", text="Civil Status")
        payroll_tree.heading("Qualified_Dependent_Status", text="Qualified Dependent status")
        payroll_tree.heading("Pay_Date", text="Pay Date")
        payroll_tree.heading("Employee_Status", text="Employee Status")
        payroll_tree.heading("Designation", text="Designation")
        payroll_tree.heading("SSS_Contribution", text="SSS Contribution")
        payroll_tree.heading("Phil_Health_Contribution", text="PhilHealth Contribution")
        payroll_tree.heading("Pag_Ibig_Contribution", text="PagIbig Contribution")
        payroll_tree.heading("Income_Tax_Contribution", text="Income Tax Contribution")
        payroll_tree.heading("SSS_Loan", text="SSS Loan")
        payroll_tree.heading("Pag_Ibig_Loan", text="PagIbig Loan")
        payroll_tree.heading("Faculty_Save_Deposit", text="Faculty Save Deposit")
        payroll_tree.heading("Faculty_Saving_Loan", text="Faculty Saving Loan")
        payroll_tree.heading("Salary_Loan", text="Salary Loan")
        payroll_tree.heading("Other_Loans", text="Other Loans")
        payroll_tree.heading("Total_Deduction", text="Total Deduction")

        # Adjust column widths for payroll Treeview
        for col in payroll_tree["columns"]:
            payroll_tree.column(col, width=55, anchor=CENTER)

        payroll_tree.pack()

        # Create a frame for the emp Treeview and scrollbar
        emp_frame = Frame(window)
        emp_frame.pack(pady=20)

        # Add a horizontal scrollbar to the emp frame
        emp_scrollbar = Scrollbar(emp_frame, orient=HORIZONTAL)
        emp_scrollbar.pack(side=BOTTOM, fill=X)

        # Create a Treeview to display emp data in a table format
        emp_tree = ttk.Treeview(emp_frame, columns=(
        "First_Name", "Middle_Name", "Last_Name", "Suffix", "Date_of_Birth", "Gender", "Nationality", "Civil_Status",
        "Department_Name", "Designation", "Dep_Status",
        "Employee_Status", "Date", "Employee_Number", "Contact_Number", "Email", "Social_Media", "Social_Media_Account",
        "Address_Line1", "Address_Line2",
        "City", "State", "Country", "Zip_Code", "Picture_Path"),
                                show='headings', xscrollcommand=emp_scrollbar.set)

        # Configure the scrollbar for emp Treeview
        emp_scrollbar.config(command=emp_tree.xview)

        # Define headings for emp Treeview
        emp_tree.heading("First_Name", text="First Name")
        emp_tree.heading("Middle_Name", text="Middle Name")
        emp_tree.heading("Last_Name", text="Last Name")
        emp_tree.heading("Suffix", text="Suffix")
        emp_tree.heading("Date_of_Birth", text="Date of Birth")
        emp_tree.heading("Gender", text="Gender")
        emp_tree.heading("Nationality", text="Nationality")
        emp_tree.heading("Civil_Status", text="Civil Status")
        emp_tree.heading("Department_Name", text="Department Name")
        emp_tree.heading("Designation", text="Designation")
        emp_tree.heading("Dep_Status", text="Department Status")
        emp_tree.heading("Employee_Status", text="Employee Status")
        emp_tree.heading("Date", text="Date")
        emp_tree.heading("Employee_Number", text="Employee_Number")
        emp_tree.heading("Contact_Number", text="Contact Number")
        emp_tree.heading("Email", text="Email")
        emp_tree.heading("Social_Media", text="Social Media")
        emp_tree.heading("Social_Media_Account", text="Social Media Account")
        emp_tree.heading("Address_Line1", text="Address Line 1")
        emp_tree.heading("Address_Line2", text="Address Line2")
        emp_tree.heading("City", text="City")
        emp_tree.heading("State", text="State")
        emp_tree.heading("Country", text="Country")
        emp_tree.heading("Zip_Code", text="Zip Code")
        emp_tree.heading("Picture_Path", text="Picture Path")

        # Adjust column widths for emp Treeview
        for col in emp_tree["columns"]:
            emp_tree.column(col, width=71, anchor=CENTER)

        emp_tree.pack()

        # Create a frame for the user Treeview and scrollbar
        user_frame = Frame(window)
        user_frame.pack(pady=20)

        # Add a horizontal scrollbar to the user frame
        user_scrollbar = Scrollbar(user_frame, orient=HORIZONTAL)
        user_scrollbar.pack(side=BOTTOM, fill=X)

        # Create a Treeview to display user data in a table format
        user_tree = ttk.Treeview(user_frame, columns=(
        "first_name", "middle_name", "last_name", "suffix", "department", "designation", "username", "password",
        "confirm_password", "user_type", "user_status", "employee_number"),
                                 show='headings', xscrollcommand=user_scrollbar.set)

        # Configure the scrollbar for user Treeview
        user_scrollbar.config(command=user_tree.xview)

        # Define headings for user Treeview
        user_tree.heading("first_name", text="First Name")
        user_tree.heading("middle_name", text="Middle Name")
        user_tree.heading("last_name", text="Last Name")
        user_tree.heading("suffix", text="Suffix")
        user_tree.heading("department", text="Department")
        user_tree.heading("designation", text="Designation")
        user_tree.heading("username", text="Username")
        user_tree.heading("password", text="Password")
        user_tree.heading("confirm_password", text="Confirm Password")
        user_tree.heading("user_type", text="User Type")
        user_tree.heading("user_status", text="User Status")
        user_tree.heading("employee_number", text="Employee Number")

        # Adjust column widths for user Treeview
        for col in user_tree["columns"]:
            user_tree.column(col, width=147, anchor=CENTER)

        user_tree.pack()


root = tk.Tk()
app = LoginSystem(root)
root.mainloop()
