import tkinter as tk
import pandas as pd

class GSTCalculatorGUI:
    def __init__(self, db):
        self.db = db

        # Create the main window
        self.window = tk.Tk()
        self.window.title("GST calculator")
        self.window.configure(bg="light blue")  # set the background color to light blue

        # Create variables for check boxes
        self.igst_var = tk.IntVar()
        self.sgst_var = tk.IntVar()
        self.cgst_var = tk.IntVar()

        # Create the widgets
        self.create_widgets()

    def create_widgets(self):
        # Create check boxes for GST types
        igst_check = tk.Checkbutton(self.window, text="IGST", variable=self.igst_var, bg="light blue", command=self.update_check)
        igst_check.grid(row=0, column=0, padx=10, pady=10)
        sgst_check = tk.Checkbutton(self.window, text="SGST", variable=self.sgst_var, bg="light blue", command=self.update_check)
        sgst_check.grid(row=0, column=1, padx=10, pady=10)
        cgst_check = tk.Checkbutton(self.window, text="CGST", variable=self.cgst_var, bg="light blue", command=self.update_check)
        cgst_check.grid(row=0, column=2, padx=10, pady=10)

        # Create labels and entry widgets for other fields
        opening_balance_label = tk.Label(self.window, text="Opening Balance:", bg="light blue")
        opening_balance_label.grid(row=1, column=0, padx=10, pady=10)
        self.opening_balance_entry = tk.Entry(self.window)
        self.opening_balance_entry.grid(row=1, column=1, padx=10, pady=10)

        input_label = tk.Label(self.window, text="Input:", bg="light blue")
        input_label.grid(row=2, column=0, padx=10, pady=10)
        self.input_entry = tk.Entry(self.window)
        self.input_entry.grid(row=2, column=1, padx=10, pady=10)

        output_label = tk.Label(self.window, text="Output:", bg="light blue")
        output_label.grid(row=3, column=0, padx=10, pady=10)
        self.output_entry = tk.Entry(self.window)
        self.output_entry.grid(row=3, column=1, padx=10, pady=10)

        transfer_label = tk.Label(self.window, text="Transfer:", bg="light blue")
        transfer_label.grid(row=4, column=0, padx=10, pady=10)
        self.transfer_entry = tk.Entry(self.window)
        self.transfer_entry.grid(row=4, column=1, padx=10, pady=10)

        closing_balance_label = tk.Label(self.window, text="Closing Balance:", bg="light blue")
        closing_balance_label.grid(row=5, column=0, padx=10, pady=10)
        self.closing_balance_entry = tk.Entry(self.window, state="readonly")
        self.closing_balance_entry.grid(row=5, column=1, padx=10, pady=10)

        sgst_paid_label = tk.Label(self.window, text="SGST Paid:", bg="light blue")
        sgst_paid_label.grid(row=6, column=0, padx=10, pady=10)
        self.sgst_paid_entry = tk.Entry(self.window, state="disabled")
        self.sgst_paid_entry.grid(row=6, column=1, padx=10, pady=10)

        # Create the submit, export, and create buttons
        submit_button = tk.Button(self.window, text="Submit", command=self.insert_data)
        submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        export_button = tk.Button(self.window, text="Export", command=self.export_data)
        export_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_closing_balance)
        calculate_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        create_button = tk.Button(self.window, text="Create", command=self.create_table)
        create_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    def run(self):
        # Start the main loop
        self.window.mainloop()

    def update_check(self):
        if self.igst_var.get():  # check if igst is checked
            self.sgst_var.set(0)  # deselect sgst
            self.cgst_var.set(0)  # deselect cgst
            self.transfer_entry.config(state="normal")  # enable transfer entry
            self.closing_balance_entry.config(state="normal")  # enable closing balance entry
            self.sgst_paid_entry.config(state="disabled")  # disable sgst paid entry
        elif self.sgst_var.get():  # check if sgst is checked
            self.igst_var.set(0)  # deselect igst
            self.cgst_var.set(0)  # deselect cgst
            self.transfer_entry.config(state="disabled")  # disable transfer entry
            self.closing_balance_entry.config(state="disabled")  # disable closing balance entry
            self.sgst_paid_entry.config(state="normal")  # enable sgst paid entry
        elif self.cgst_var.get():  # check if cgst is checked
            self.igst_var.set(0)  # deselect igst
            self.sgst_var.set(0)  # deselect sgst
            self.transfer_entry.config(state="normal")  # enable transfer entry
            self.closing_balance_entry.config(state="normal")  # enable closing balance entry
            self.sgst_paid_entry.config(state="disabled")  # disable sgst paid entry

    def insert_data(self):
        gst = ""  # initialize an empty string for gst
        if self.igst_var.get():  # check if the igst check box is checked
            gst += "IGST "  # append "IGST " to the gst string
        if self.sgst_var.get():  # check if the sgst check box is checked
            gst += "SGST "  # append "SGST " to the gst string
        if self.cgst_var.get():  # check if the cgst check box is checked
            gst += "CGST "  # append "CGST " to the gst string
        opening_balance = self.opening_balance_entry.get()  # get the opening balance from the entry widget
        input_val = self.input_entry.get()  # get the input from the entry widget
        output = self.output_entry.get()  # get the output from the entry widget
        transfer = self.transfer_entry.get()  # get the transfer from the entry widget

        if not transfer:
            transfer = "0"  # Set transfer to 0 if it is empty

        closing_balance = int(opening_balance) + int(input_val) - int(output) - int(transfer)  # calculate the closing balance using the logic
        if "SGST" in gst:  # check if the gst contains SGST
            sgst_paid = -closing_balance  # calculate the sgst paid using the logic
        else:  # otherwise
            sgst_paid = 0  # set the sgst paid to zero
        self.db.insert_data(gst, opening_balance, input_val, output, transfer, closing_balance, sgst_paid)  # insert the data into the table
        self.clear_entries()

    def export_data(self):
        data = self.db.export_data()
        df = pd.DataFrame(data)
        df.to_excel("form.xlsx", index=False)  # write the DataFrame to an Excel file

    def create_table(self):
        table_data = self.db.fetch_data()
        table_window = tk.Toplevel(self.window)  # create a new window for the table
        table_window.title("Table Window")
        table_window.configure(bg="light blue")  # set the background color to light blue
        for i, row in enumerate(table_data):
            for j, value in enumerate(row):
                cell = tk.Label(table_window, text=value, bg="light blue")  # create a label for each cell of the table
                cell.grid(row=i, column=j, padx=10, pady=10)  # place the label in the grid layout

    def calculate_closing_balance(self):
        gst = ""
        if self.igst_var.get():
            gst += "IGST "
        if self.sgst_var.get():
            gst += "SGST "
        if self.cgst_var.get():
            gst += "CGST "

        opening_balance = self.opening_balance_entry.get()
        input_val = self.input_entry.get()
        output = self.output_entry.get()
        transfer = self.transfer_entry.get()

        if not transfer:
            transfer = "0"  # Set transfer to 0 if it is empty

        closing_balance = int(opening_balance) + int(input_val) - int(output) - int(transfer)

        if "SGST" in gst:
            sgst_paid = -closing_balance
        else:
            sgst_paid = 0

        self.closing_balance_entry.config(state="normal")
        self.closing_balance_entry.delete(0, tk.END)
        self.closing_balance_entry.insert(tk.END, closing_balance)
        self.closing_balance_entry.config(state="readonly")

        self.sgst_paid_entry.config(state="normal")
        self.sgst_paid_entry.delete(0, tk.END)
        self.sgst_paid_entry.insert(tk.END, sgst_paid)
        self.sgst_paid_entry.config(state="disabled")

    def clear_entries(self):
        self.opening_balance_entry.delete(0, tk.END)  # clear the opening balance entry
        self.input_entry.delete(0, tk.END)  # clear the input entry
        self.output_entry.delete(0, tk.END)  # clear the output entry
        self.transfer_entry.delete(0, tk.END)  # clear the transfer entry

    # ... other methods of the GUI class
