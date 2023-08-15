# GST Calculator

The GST Calculator is a simple application built using Python and Tkinter that enables users to calculate GST (Goods and Services Tax) values and manage associated financial data. This application features a user-friendly graphical interface for entering input values, performing calculations, and storing data in a SQLite database. Users can also export data to an Excel file for further analysis or reporting.

## Features

- Calculate GST values based on user input.
- Store calculated data in a SQLite database.
- Export data to an Excel file for further analysis or reporting.
- View stored data in a tabular format within the application.
- Intuitive GUI designed using Tkinter.

## Requirements

- Python 3.6 or higher
- Tkinter package (usually included with Python installation)
- SQLite3 package (usually included with Python installation)
- Pandas package (`pip install pandas`)

## Installation

1. Clone the repository or download the source code as a ZIP file.
2. Navigate to the project directory:

```bash
cd GST_Calculator
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
7. Click the "Create" button to view the stored data in a tabular format within the application.
8. The database file (`form.db`) will be created in the project directory to store the data.

## Contributing

Contributions to the GST Calculator project are welcome! If you encounter issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README template according to your project's needs. You can add extra sections like "Troubleshooting," "Testing," or "Acknowledgments" as required.
