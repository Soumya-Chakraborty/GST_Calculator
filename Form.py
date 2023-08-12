import tkinter as tk
import sqlite3
import pandas as pd

# Create the database connection and cursor
conn = sqlite3.connect("form.db")  # create or connect to a database file
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS gst (gst TEXT, opening_balance INTEGER, input INTEGER, output INTEGER, transfer INTEGER, closing_balance INTEGER, sgst_paid INTEGER)")  # create a table if not exists

# Define the function to insert data into the database
def insert_data():
    gst = ""  # initialize an empty string for gst
    if igst_var.get():  # check if the igst check box is checked
        gst += "IGST "  # append "IGST " to the gst string
    if sgst_var.get():  # check if the sgst check box is checked
        gst += "SGST "  # append "SGST " to the gst string
    if cgst_var.get():  # check if the cgst check box is checked
        gst += "CGST "  # append "CGST " to the gst string
    opening_balance = opening_balance_entry.get()  # get the opening balance from the entry widget
    input_val = input_entry.get()  # get the input from the entry widget
    output = output_entry.get()  # get the output from the entry widget
    transfer = transfer_entry.get()  # get the transfer from the entry widget
    
    if not transfer:
        transfer = "0"  # Set transfer to 0 if it is empty
    
    closing_balance = int(opening_balance) + int(input_val) - int(output) - int(transfer)  # calculate the closing balance using the logic
    if "SGST" in gst:  # check if the gst contains SGST
        sgst_paid = -closing_balance  # calculate the sgst paid using the logic
    else:  # otherwise
        sgst_paid = 0  # set the sgst paid to zero
    cur.execute("INSERT INTO gst VALUES (?, ?, ?, ?, ?, ?, ?)",
                (gst, opening_balance, input_val, output, transfer, closing_balance, sgst_paid))  # insert the data into the table
    conn.commit()  # save the changes
    opening_balance_entry.delete(0, tk.END)  # clear the opening balance entry
    input_entry.delete(0, tk.END)  # clear the input entry
    output_entry.delete(0, tk.END)  # clear the output entry
    transfer_entry.delete(0, tk.END)  # clear the transfer entry

# Define the function to export data to an excel sheet
def export_data():
    cur.execute("SELECT * FROM gst")  # execute SQL query directly with the cursor
    rows = cur.fetchall()  # fetch all rows from the cursor

    columns = [description[0] for description in cur.description]  # get column names from cursor description

    df = pd.DataFrame(rows, columns=columns)  # create a DataFrame from the fetched rows and column names
    df = df.transpose()  # Transpose the DataFrame to convert columns into rows
    df.to_excel("form.xlsx", index=False)  # write the DataFrame to an Excel file

# Define the function to create a table in the GUI
def create_table():
    df = pd.read_sql_query("SELECT * FROM gst", conn)  # read the data from the table into a dataframe
    rows, columns = df.shape  # get the number of rows and columns of the dataframe
    table_window = tk.Toplevel(window)  # create a new window for the table
    table_window.title("Table Window")
    table_window.configure(bg="light blue")  # set the background color to light blue
    for i in range(rows):  # loop through each row of the dataframe
        for j in range(columns):  # loop through each column of the dataframe
            cell = tk.Label(table_window, text=df.iloc[i, j], bg="light blue")  # create a label for each cell of the dataframe
            cell.grid(row=i, column=j, padx=10, pady=10)  # place the label in the grid layout

# Create the main window
window = tk.Tk()
window.title("GST calculator")
window.configure(bg="light blue")  # set the background color to light blue

# Create variables for check boxes
igst_var = tk.IntVar()
sgst_var = tk.IntVar()
cgst_var = tk.IntVar()

# Function to update check boxes
def update_check():
    if igst_var.get():  # check if igst is checked
        sgst_check.deselect()  # deselect sgst
        cgst_check.deselect()  # deselect cgst
        transfer_entry.config(state="normal")  # enable transfer entry
        closing_balance_entry.config(state="normal")  # enable closing balance entry
        sgst_paid_entry.config(state="disabled")  # disable sgst paid entry
    elif sgst_var.get():  # check if sgst is checked
        igst_check.deselect()  # deselect igst
        cgst_check.deselect()  # deselect cgst
        transfer_entry.config(state="disabled")  # disable transfer entry
        closing_balance_entry.config(state="disabled")  # disable closing balance entry
        sgst_paid_entry.config(state="normal")  # enable sgst paid entry
    elif cgst_var.get():  # check if cgst is checked
        igst_check.deselect()  # deselect igst
        sgst_check.deselect()  # deselect sgst
        transfer_entry.config(state="normal")  # enable transfer entry
        closing_balance_entry.config(state="normal")  # enable closing balance entry
        sgst_paid_entry.config(state="disabled")  # disable sgst paid entry

# Create check boxes for GST types
igst_check = tk.Checkbutton(window, text="IGST", variable=igst_var, bg="light blue", command=update_check)
igst_check.grid(row=0, column=0, padx=10, pady=10)
sgst_check = tk.Checkbutton(window, text="SGST", variable=sgst_var, bg="light blue", command=update_check)
sgst_check.grid(row=0, column=1, padx=10, pady=10)
cgst_check = tk.Checkbutton(window, text="CGST", variable=cgst_var, bg="light blue", command=update_check)
cgst_check.grid(row=0, column=2, padx=10, pady=10)

# Create labels and entry widgets for other fields
opening_balance_label = tk.Label(window, text="Opening Balance:", bg="light blue")
opening_balance_label.grid(row=1, column=0, padx=10, pady=10)
opening_balance_entry = tk.Entry(window)
opening_balance_entry.grid(row=1, column=1, padx=10, pady=10)

input_label = tk.Label(window, text="Input:", bg="light blue")
input_label.grid(row=2, column=0, padx=10, pady=10)
input_entry = tk.Entry(window)
input_entry.grid(row=2, column=1, padx=10, pady=10)

output_label = tk.Label(window, text="Output:", bg="light blue")
output_label.grid(row=3, column=0, padx=10, pady=10)
output_entry = tk.Entry(window)
output_entry.grid(row=3, column=1, padx=10, pady=10)

transfer_label = tk.Label(window, text="Transfer:", bg="light blue")
transfer_label.grid(row=4, column=0, padx=10, pady=10)
transfer_entry = tk.Entry(window)
transfer_entry.grid(row=4, column=1, padx=10, pady=10)

closing_balance_label = tk.Label(window, text="Closing Balance:", bg="light blue")
closing_balance_label.grid(row=5, column=0, padx=10, pady=10)
closing_balance_entry = tk.Entry(window, state="readonly")
closing_balance_entry.grid(row=5, column=1, padx=10, pady=10)

sgst_paid_label = tk.Label(window, text="SGST Paid:", bg="light blue")
sgst_paid_label.grid(row=6, column=0, padx=10, pady=10)
sgst_paid_entry = tk.Entry(window, state="disabled")
sgst_paid_entry.grid(row=6, column=1, padx=10, pady=10)

# Function to calculate the closing balance
def calculate_closing_balance():
    gst = ""
    if igst_var.get():
        gst += "IGST "
    if sgst_var.get():
        gst += "SGST "
    if cgst_var.get():
        gst += "CGST "
        
    opening_balance = opening_balance_entry.get()
    input_val = input_entry.get()
    output = output_entry.get()
    transfer = transfer_entry.get()
    
    if not transfer:
        transfer = "0"  # Set transfer to 0 if it is empty
    
    closing_balance = int(opening_balance) + int(input_val) - int(output) - int(transfer)
    
    if "SGST" in gst:
        sgst_paid = -closing_balance
    else:
        sgst_paid = 0
        
    closing_balance_entry.config(state="normal")
    closing_balance_entry.delete(0, tk.END)
    closing_balance_entry.insert(tk.END, closing_balance)
    closing_balance_entry.config(state="readonly")
    
    sgst_paid_entry.config(state="normal")
    sgst_paid_entry.delete(0, tk.END)
    sgst_paid_entry.insert(tk.END, sgst_paid)
    sgst_paid_entry.config(state="disabled")

# Create the submit, export, and create buttons
submit_button = tk.Button(window, text="Submit", command=insert_data)
submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

export_button = tk.Button(window, text="Export", command=export_data)
export_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate", command=calculate_closing_balance)
calculate_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

create_button = tk.Button(window, text="Create", command=create_table)
create_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
window.mainloop()

# Close the database connection
conn.close()