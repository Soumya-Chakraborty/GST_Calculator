# GST Calculator

The GST Calculator is a simple application built using Python and Tkinter that allows users to calculate GST (Goods and Services Tax) values and manage the associated financial data. The application provides a user-friendly graphical interface for entering input values, performing calculations, and storing the data in a SQLite database. Users can also export the data to an Excel file for further analysis or reporting.

## Features

- Calculate GST values based on user input.
- Store the calculated data in a SQLite database.
- Export the data to an Excel file for further analysis or reporting.
- View the stored data in a table format within the application.
- Intuitive GUI built using Tkinter.

## Requirements

- Python 3.6 or higher
- Tkinter package (usually included with Python installation)
- SQLite3 package (usually included with Python installation)
- Pandas package (`pip install pandas`)

## Installation

1. Clone the repository or download the source code as a ZIP file.
2. Navigate to the project directory:

```bash
cd GST
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python main.py
```

2. The GST Calculator GUI will open.
3. Enter the opening balance, input, output, and transfer values.
4. Check the applicable GST types (IGST, SGST, CGST).
5. Click the "Submit" button to calculate and store the data.
6. Use the "Export" button to export the data to an Excel file.
7. Click the "Create" button to view the stored data in a table format within the application.
8. The database file (`form.db`) will be created in the project directory to store the data.

## Contributing

Contributions to the GST Calculator project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README template to fit your project requirements. You can add more sections such as "Troubleshooting," "Testing," or "Acknowledgments" based on your project's specific needs.
