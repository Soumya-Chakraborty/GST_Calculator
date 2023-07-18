from gst_gui import GSTCalculatorGUI
from gst_db import GSTDatabase

def main():
    # Create the database connection and cursor
    db = GSTDatabase("form.db")
    db.create_table()

    # Create the GUI
    gst_gui = GSTCalculatorGUI(db)
    gst_gui.run()

    # Close the database connection
    db.close()

if __name__ == '__main__':
    main()
