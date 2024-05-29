import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3

def create_payroll_window(master):
    con = sqlite3.connect("Laboratory8")
    cursor = con.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Payroll (
        Employee_Number TEXT PRIMARY KEY,
        Department TEXT,
        Rate_1 REAL,
        Hour_1 REAL,
        Income_1 REAL,
        Rate_2 REAL,
        Hour_2 REAL,
        Income_2 REAL,
        Rate_3 REAL,
        Hour_3 REAL,
        Income_3 REAL,
        Gross_income REAL,
        Net_income REAL,
        First_name TEXT,
        Middle_name TEXT,
        Surname TEXT,
        Civil_Status TEXT,
        Qualified_Dependent_Status TEXT,
        Pay_Date TEXT,
        Employee_Status TEXT,
        Designation TEXT,
        SSS_Contribution REAL,
        Phil_Health_Contribution REAL,
        Pag_Ibig_Contribution REAL,
        Income_Tax_Contribution REAL,
        SSS_Loan REAL,
        Pag_Ibig_Loan REAL,
        Faculty_Save_Deposit REAL,
        Faculty_Saving_Loan REAL,
        Salary_Loan REAL,
        Other_Loans REAL,
        Total_Deduction REAL
    )
    ''')

    window = master
    window.title("Payroll System")
    window.geometry("1900x1080")

    bg_image = Image.open("C:/GUI/blue.jpg")
    bg_image = bg_image.resize((1920, 1100))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def save_data_entry():
        employee_no = employee_no_entry.get()
        department = department_entry.get()
        rate1 = rate1_entry.get()
        hour1 = hour1_entry.get()
        income1 = income1_entry.get()
        rate2 = rate2_entry.get()
        hour2 = hour2_entry.get()
        income2 = income2_entry.get()
        rate3 = rate3_entry.get()
        hour3 = hour3_entry.get()
        income3 = income3_entry.get()
        gross_income = gross_entry.get()
        net_income = net_entry.get()
        first_name = first_entry.get()
        middle_name = middle_entry.get()
        surname = surname_entry.get()
        civil_status = civil_entry.get()
        qualified_dependent_status = qualified_entry.get()
        pay_date = paydate_entry.get()
        employee_status = status_entry.get()
        designation = designation_entry.get()
        sss_contribution = SSS_entry.get()
        phil_health_contribution = ph_entry.get()
        pag_ibig_contribution = pagibig_entry.get()
        income_tax_contribution = income_tax_entry.get()
        sss_loan = SSS1_entry.get()
        pag_ibig_loan = pagibig1_entry.get()
        faculty_save_deposit = faculty_entry.get()
        faculty_saving_loan = faculty_loan_entry.get()
        salary_loan = salary_entry.get()
        other_loans = loan_entry.get()
        total_deduction = total_entry.get()

        save_data_query = (
            "INSERT OR REPLACE INTO Payroll (Employee_Number, Department, Rate_1, Hour_1, Income_1, Rate_2, Hour_2, Income_2, Rate_3, Hour_3, Income_3, Gross_income, Net_income, First_name, Middle_name, Surname, Civil_Status, Qualified_Dependent_Status, Pay_Date, Employee_Status, Designation, SSS_Contribution, Phil_Health_Contribution, Pag_Ibig_Contribution, Income_Tax_Contribution, SSS_Loan, Pag_Ibig_Loan, Faculty_Save_Deposit, Faculty_Saving_Loan, Salary_Loan, Other_Loans, Total_Deduction) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        )

        con.execute(save_data_query, (
            employee_no, department, rate1, hour1, income1, rate2, hour2, income2, rate3, hour3, income3, gross_income,
            net_income, first_name, middle_name, surname, civil_status, qualified_dependent_status, pay_date, employee_status,
            designation, sss_contribution, phil_health_contribution, pag_ibig_contribution, income_tax_contribution, sss_loan,
            pag_ibig_loan, faculty_save_deposit, faculty_saving_loan, salary_loan, other_loans, total_deduction
        ))
        con.commit()
        messagebox.showinfo(title="Data Saved", message="Data has been saved to SQL")
        print("\nData saved...........")

    def search_employee():
        employee_number = employee_no_entry.get()
        cursor.execute("SELECT * FROM emp_tbl WHERE Employee_Number=?", (employee_number,))
        row = cursor.fetchone()
        if row:
            department_entry.delete(0, tk.END)
            department_entry.insert(0, row[5])
            first_entry.delete(0, tk.END)
            first_entry.insert(0, row[1])
            middle_entry.delete(0, tk.END)
            middle_entry.insert(0, row[2])
            surname_entry.delete(0, tk.END)
            surname_entry.insert(0, row[3])
            status_entry.delete(0, tk.END)
            status_entry.insert(0, row[12])
            qualified_entry.delete(0, tk.END)
            qualified_entry.insert(0, row[11])
            civil_entry.delete(0, tk.END)
            civil_entry.insert(0, row[8])
            designation_entry.delete(0, tk.END)
            designation_entry.insert(0, row[10])
            paydate_entry.delete(0, tk.END)
            paydate_entry.insert(0, row[13])


            print("Employee data loaded successfully!")
        else:
            messagebox.showwarning("Warning", "Employee number not found!")

    font_style = ("Times New Roman", 12, "bold")
    font = ("Times New Roman", 12)

    main_frame = tk.Frame(window)
    main_frame.config(bg="white")
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    user_info_frame = tk.LabelFrame(main_frame, text="")
    user_info_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    user_frame = tk.Frame(user_info_frame)
    user_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")

#employee
    employee_label = tk.Label(user_frame, text="EMPLOYEE PAYROLL", font=("Times New Roman", 15, "bold"))
    employee_label.grid(row=0, column=0, sticky='w')

    image_frame = tk.Frame(user_frame)
    image_frame.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    default_image = Image.open("C:\\GUI\\defaultphoto.jpg")
    default_image = default_image.resize((150, 150))
    default_photo = ImageTk.PhotoImage(default_image)
    image_label = tk.Label(image_frame, image=default_photo)
    image_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    employee_no = tk.Label(user_frame, text='Employee number', font=font)
    employee_no.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    img_select = tk.Label(user_frame, text="Search employee", font=font)
    img_select.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    department = tk.Label(user_frame, text=" Department ", font=font)
    department.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    basic_inc = tk.Label(user_frame, text="BASIC INCOME:", font=font_style)
    basic_inc.grid(row=5, column=0, pady=19, sticky="w")

    rate1 = tk.Label(user_frame, text="Rate/hour", font=font)
    rate1.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    hour1 = tk.Label(user_frame, text="No. of hours/cut off", font=font)
    hour1.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    income1 = tk.Label(user_frame, text="Income cut/off", font=font)
    income1.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    hon_inc = tk.Label(user_frame, text="HONORARIUM INCOME:", font=font_style)
    hon_inc.grid(row=9, column=0, pady=10, sticky="w")

    rate2 = tk.Label(user_frame, text="Rate/hour", font=font)
    rate2.grid(row=10, column=0, padx=5, pady=5, sticky="w")

    hour2 = tk.Label(user_frame, text="No. of hours/cut off", font=font)
    hour2.grid(row=11, column=0, padx=5, pady=5, sticky="w")

    income2 = tk.Label(user_frame, text="Income cut/off", font=font)
    income2.grid(row=12, column=0, padx=5, pady=5, sticky="w")

    oth_inc = tk.Label(user_frame, text="OTHER INCOME:", font=font_style)
    oth_inc.grid(row=13, column=0, pady=19, sticky="w")

    rate3 = tk.Label(user_frame, text="Rate/hour", font=font)
    rate3.grid(row=14, column=0, padx=5, pady=5, sticky="w")

    hour3 = tk.Label(user_frame, text="No. of hours/cut off", font=font)
    hour3.grid(row=15, column=0, padx=5, pady=5, sticky="w")

    income3 = tk.Label(user_frame, text="Income cut/off", font=font)
    income3.grid(row=16, column=0, padx=5, pady=5, sticky="w")

    sum_inc = tk.Label(user_frame, text="SUMMARY INCOME:", font=font_style)
    sum_inc.grid(row=17, column=0, pady=19, sticky="w")

    gross = tk.Label(user_frame, text="Gross Income", font=font)
    gross.grid(row=18, column=0, padx=5, pady=5, sticky="w")

    net = tk.Label(user_frame, text="Net income", font=font)
    net.grid(row=19, column=0, padx=5, pady=5, sticky="w")

    employee_no_entry = tk.Entry(user_frame, font=font, width=20)
    employee_no_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    search_image_button = ttk.Button(user_frame, text="Search", command=search_employee, cursor="hand2")
    search_image_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    department_entry = tk.Entry(user_frame, font=font, width=20)
    department_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    rate1_entry = tk.Entry(user_frame, font=font, width=20)
    rate1_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    hour1_entry = tk.Entry(user_frame, font=font, width=20)
    hour1_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    income1_entry = tk.Entry(user_frame, font=font, width=20)
    income1_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    rate2_entry = tk.Entry(user_frame, font=font, width=20)
    rate2_entry.grid(row=10, column=1, padx=5, pady=5, sticky="w")

    hour2_entry = tk.Entry(user_frame, font=font, width=20)
    hour2_entry.grid(row=11, column=1, padx=5, pady=5, sticky="w")

    income2_entry = tk.Entry(user_frame, font=font, width=20)
    income2_entry.grid(row=12, column=1, padx=5, pady=5, sticky="w")

    rate3_entry = tk.Entry(user_frame, font=font, width=20)
    rate3_entry.grid(row=14, column=1, padx=5, pady=5, sticky="w")

    hour3_entry = tk.Entry(user_frame, font=font, width=20)
    hour3_entry.grid(row=15, column=1, padx=5, pady=5, sticky="w")

    income3_entry = tk.Entry(user_frame, font=font, width=20)
    income3_entry.grid(row=16, column=1, padx=5, pady=5, sticky="w")

    gross_entry = tk.Entry(user_frame, font=font, width=20)
    gross_entry.grid(row=18, column=1, padx=5, pady=5, sticky="w")

    net_entry = tk.Entry(user_frame, font=font, width=20)
    net_entry.grid(row=19, column=1, padx=5, pady=5, sticky="w")

    user_frame2 = tk.Frame(user_info_frame)
    user_frame2.grid(row=0, column=2, padx=50, pady=5, sticky="nw")

    first = tk.Label(user_frame2, text="First name", font=font)
    first.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    middle = tk.Label(user_frame2, text="Middle name", font=font)
    middle.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    surname = tk.Label(user_frame2, text="Surnname", font=font)
    surname.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    civil = tk.Label(user_frame2, text="Civil status", font=font)
    civil.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    qualified = tk.Label(user_frame2, text="Qualified dependent \nstatus", font=font)
    qualified.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    paydate = tk.Label(user_frame2, text="Paydate", font=font)
    paydate.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    status = tk.Label(user_frame2, text="employee status", font=font)
    status.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    designation = tk.Label(user_frame2, text="designation", font=font)
    designation.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    oth_inc = tk.Label(user_frame2, text="REGULAR DEDUCTION:", font=font_style)
    oth_inc.grid(row=8, column=0, pady=19, sticky="w")

    SSS = tk.Label(user_frame2, text="SSS contribution", font=font)
    SSS.grid(row=9, column=0, padx=5, pady=5, sticky="w")

    ph = tk.Label(user_frame2, text="Phil-health contribution", font=font)
    ph.grid(row=10, column=0, padx=5, pady=5, sticky="w")

    pagibig = tk.Label(user_frame2, text="pag ibig contribution", font=font)
    pagibig.grid(row=11, column=0, padx=5, pady=5, sticky="w")

    income_tax = tk.Label(user_frame2, text="Income tax Contribution", font=font)
    income_tax.grid(row=12, column=0, padx=5, pady=5, sticky="w")

    oth_inc = tk.Label(user_frame2, text="OTHER DEDUCTION:", font=font_style)
    oth_inc.grid(row=13, column=0, pady=19, sticky="w")

    SSS1 = tk.Label(user_frame2, text="SSS Loan", font=font)
    SSS1.grid(row=14, column=0, padx=5, pady=5, sticky="w")

    pagibig1 = tk.Label(user_frame2, text="pagibig loan", font=font)
    pagibig1.grid(row=15, column=0, padx=5, pady=5, sticky="w")

    faculty = tk.Label(user_frame2, text="Faculty saving deposit", font=font)
    faculty.grid(row=16, column=0, padx=5, pady=5, sticky="w")

    faculty_loan = tk.Label(user_frame2, text="faculty saving loan", font=font)
    faculty_loan.grid(row=17, column=0, padx=5, pady=5, sticky="w")

    salary = tk.Label(user_frame2, text="salary loan", font=font)
    salary.grid(row=18, column=0, padx=5, pady=5, sticky="w")

    loan = tk.Label(user_frame2, text="Other loans", font=font)
    loan.grid(row=19, column=0, padx=5, pady=5, sticky="w")

    oth_inc = tk.Label(user_frame2, text="DEDUCTION SUMMARY:", font=font_style)
    oth_inc.grid(row=20, column=0, pady=19, sticky="w")

    total = tk.Label(user_frame2, text="Total deduction", font=font)
    total.grid(row=21, column=0, padx=5, pady=5, sticky="w")

    first_entry = tk.Entry(user_frame2, font=font, width=20)
    first_entry.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    middle_entry = tk.Entry(user_frame2, font=font, width=20)
    middle_entry.grid(row=1, column=2, padx=5, pady=5, sticky="w")

    surname_entry = tk.Entry(user_frame2, font=font, width=20)
    surname_entry.grid(row=2, column=2, padx=5, pady=5, sticky="w")

    civil_entry = tk.Entry(user_frame2, font=font, width=20)
    civil_entry.grid(row=3, column=2, padx=5, pady=5, sticky="w")

    qualified_entry = tk.Entry(user_frame2, font=font, width=20)
    qualified_entry.grid(row=4, column=2, padx=5, pady=5, sticky="w")

    paydate_entry = tk.Entry(user_frame2, font=font, width=20)
    paydate_entry.grid(row=5, column=2, padx=5, pady=5, sticky="w")

    status_entry = tk.Entry(user_frame2, font=font, width=20)
    status_entry.grid(row=6, column=2, padx=5, pady=5, sticky="w")

    designation_entry = tk.Entry(user_frame2, font=font, width=20)
    designation_entry.grid(row=7, column=2, padx=5, pady=5, sticky="w")

    SSS_entry = tk.Entry(user_frame2, font=font, width=20)
    SSS_entry.grid(row=9, column=2, padx=5, pady=5, sticky="w")

    ph_entry = tk.Entry(user_frame2, font=font, width=20)
    ph_entry.grid(row=10, column=2, padx=5, pady=5, sticky="w")

    pagibig_entry = tk.Entry(user_frame2, font=font, width=20)
    pagibig_entry.grid(row=11, column=2, padx=5, pady=5, sticky="w")

    income_tax_entry = tk.Entry(user_frame2, font=font, width=20)
    income_tax_entry.grid(row=12, column=2, padx=5, pady=5, sticky="w")

    SSS1_entry = tk.Entry(user_frame2, font=font, width=20)
    SSS1_entry.grid(row=14, column=2, padx=5, pady=5, sticky="w")

    pagibig1_entry = tk.Entry(user_frame2, font=font, width=20)
    pagibig1_entry.grid(row=15, column=2, padx=5, pady=5, sticky="w")

    faculty_entry = tk.Entry(user_frame2, font=font, width=20)
    faculty_entry.grid(row=16, column=2, padx=5, pady=5, sticky="w")

    faculty_loan_entry = tk.Entry(user_frame2, font=font, width=20)
    faculty_loan_entry.grid(row=17, column=2, padx=5, pady=5, sticky="w")

    salary_entry = tk.Entry(user_frame2, font=font, width=20)
    salary_entry.grid(row=18, column=2, padx=5, pady=5, sticky="w")

    loan_entry = tk.Entry(user_frame2, font=font, width=20)
    loan_entry.grid(row=19, column=2, padx=5, pady=5, sticky="w")

    total_entry = tk.Entry(user_frame2, font=font, width=20)
    total_entry.grid(row=21, column=2, padx=5, pady=5, sticky="w")

    user_frame3 = tk.Frame(user_info_frame)
    user_frame3.grid(row=1, column=2, padx=5, sticky="nw")

    def netIncome():
        gross = float(gross_entry.get())

        # ---------- SSS Contribution Computation ---------- #
        sss_con, g_var = 180.00, gross

        while sss_con < 900.00 and g_var >= 4250:
            g_var -= 500.00
            sss_con += 22.50

        SSS_entry.config(state="normal")
        SSS_entry.delete(0, "end")
        SSS_entry.insert(0, f"{sss_con}")
        SSS_entry.config(state="readonly")

        # ---------- PhilHealth contribution ---------- #
        s_co = paydate_entry.get().split("/")
        salary_cutoff_year = int(s_co[2])

        if salary_cutoff_year == 2019:
            premium_rate = 0.0275
            upper_value = 50000
        elif salary_cutoff_year == 2020:
            premium_rate = 0.03
            upper_value = 60000
        elif salary_cutoff_year == 2021:
            premium_rate = 0.035
            upper_value = 70000
        elif salary_cutoff_year == 2022:
            premium_rate = 0.04
            upper_value = 80000
        elif salary_cutoff_year == 2023:
            premium_rate = 0.045
            upper_value = 90000
        else:  # for years 2024-2025
            premium_rate = 0.05
            upper_value = 100000

        if gross <= 10000:
            philhealth_con = 10000 * premium_rate
            # if gross earnings is less than PhP 10,000, a fixed value is deducted
        elif 10000 > gross > upper_value:
            philhealth_con = gross * premium_rate
            # if gross earnings is more than 10k but less than the upper value,
            # the contribution is based on a percentage of the premium rate
        else:
            philhealth_con = upper_value * premium_rate
            #  if gross earnings is higher than year's upper value (e.g. year 2024 = 100,000),
            #  a fixed value is also deducted

        ph_entry.config(state="normal")
        ph_entry.delete(0, "end")
        ph_entry.insert(0, f"{philhealth_con}")
        ph_entry.config(state="readonly")

        # ----------Withholding Tax ---------- #
        if 0.00 < gross <= 10417.00:
            withholding_tax = 0
        elif 10417.00 < gross <= 16666.00:
            over = gross - 10417.00
            withholding_tax = 0 + (over * 0.15)
        elif 16666.00 < gross <= 33332.00:
            over = gross - 16667.00
            withholding_tax = 937.50 + (over * 0.2)
        elif 33332.00 < gross <= 83332.00:
            over = gross - 33333.00
            withholding_tax = 4270.70 + (over * 0.25)
        elif 83332.00 < gross <= 333332.00:
            over = gross - 83333.00
            withholding_tax = 16770.70 + (over * 0.3)
        else:  # for gross pay equal to 333,333 and above
            over = gross - 333333.00
            withholding_tax = 91770.70 + (over * 0.35)

        income_tax_entry.config(state="normal")
        income_tax_entry.delete(0, "end")
        income_tax_entry.insert(0, f"{withholding_tax}")
        income_tax_entry.config(state="readonly")

        pagibig_entry.config(state="normal")
        pagibig_entry.delete(0, "end")
        pagibig_entry.insert(0, "100")
        pagibig_entry.config(state="readonly")

        deduction = float(sss_con + philhealth_con + withholding_tax + 100)

        deduction += float(loan_entry.get())
        deduction += float(pagibig_entry.get())
        deduction += float(faculty_loan_entry.get())
        deduction += float(faculty_loan_entry.get())
        deduction += float(faculty_loan_entry.get())

        total_entry.config(state="normal")
        total_entry.delete(0, "end")
        total_entry.insert(0, f"{deduction}")
        total_entry.config(state="readonly")

        net_entry.config(state="normal")
        net_entry.delete(0, "end")
        net_entry.insert(0, f"{gross - deduction}")
        net_entry.config(state="readonly")

    def grossIncome():
        income_0 = float(rate1_entry.get()) * float(hour1_entry.get())
        income_1 = float(rate2_entry.get()) * float(hour2_entry.get())
        income_2 = float(rate3_entry.get()) * float(hour3_entry.get())
        gross_income = income_0 + income_1 + income_2
        gross_entry.insert(0, gross_income)

        income1_entry.insert(0, income_0)
        income2_entry.insert(0, income_1)
        income3_entry.insert(0, income_2)

    def clear_entries():
        employee_no_entry.delete(0, tk.END)
        department_entry.delete(0, tk.END)
        rate1_entry.delete(0, tk.END)
        hour1_entry.delete(0, tk.END)
        income1_entry.delete(0, tk.END)
        rate2_entry.delete(0, tk.END)
        hour2_entry.delete(0, tk.END)
        income2_entry.delete(0, tk.END)
        rate3_entry.delete(0, tk.END)
        hour3_entry.delete(0, tk.END)
        income3_entry.delete(0, tk.END)
        gross_entry.delete(0, tk.END)
        net_entry.delete(0, tk.END)
        first_entry.delete(0, tk.END)
        middle_entry.delete(0, tk.END)
        surname_entry.delete(0, tk.END)
        civil_entry.delete(0, tk.END)
        qualified_entry.delete(0, tk.END)
        paydate_entry.delete(0, tk.END)
        status_entry.delete(0, tk.END)
        designation_entry.delete(0, tk.END)
        SSS_entry.delete(0, tk.END)
        ph_entry.delete(0, tk.END)
        pagibig_entry.delete(0, tk.END)
        income_tax_entry.delete(0, tk.END)
        SSS1_entry.delete(0, tk.END)
        pagibig1_entry.delete(0, tk.END)
        faculty_entry.delete(0, tk.END)
        faculty_loan_entry.delete(0, tk.END)
        salary_entry.delete(0, tk.END)
        loan_entry.delete(0, tk.END)
        total_entry.delete(0, tk.END)

    gross_income_button = tk.Button(user_frame3, text="Gross Income", font=("Times New Roman", 12), bg="red", fg="white", cursor="hand2", command=grossIncome)
    gross_income_button.grid(row=22, column=0, padx=5, sticky="s")

    net_income_button = tk.Button(user_frame3, text="Net Income", font=("Times New Roman", 12), bg="blue", fg="white", cursor="hand2", command=netIncome)
    net_income_button.grid(row=22, column=1, padx=5, sticky="s")

    save_button = tk.Button(user_frame3, text="Save", font=("Times New Roman", 12), bg="cyan", cursor="hand2", command=save_data_entry)
    save_button.grid(row=22, column=3, padx=5, sticky="s")

    new_button = tk.Button(user_frame3, text="New", font=("Times New Roman", 12), bg="yellow", cursor="hand2", command=clear_entries)
    new_button.grid(row=22, column=5, padx=5, sticky="n")

    window.mainloop()

def Payroll(master):
    create_payroll_window(master)
