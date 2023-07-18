import sqlite3

class GSTDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS gst (gst TEXT, opening_balance INTEGER, input INTEGER, output INTEGER, transfer INTEGER, closing_balance INTEGER, sgst_paid INTEGER)")

    def insert_data(self, gst, opening_balance, input_val, output, transfer, closing_balance, sgst_paid):
        self.cur.execute("INSERT INTO gst VALUES (?, ?, ?, ?, ?, ?, ?)",
                         (gst, opening_balance, input_val, output, transfer, closing_balance, sgst_paid))
        self.conn.commit()

    def export_data(self):
        self.cur.execute("SELECT * FROM gst")
        rows = self.cur.fetchall()
        return rows

    def fetch_data(self):
        self.cur.execute("SELECT * FROM gst")
        rows = self.cur.fetchall()
        return rows

    def close(self):
        self.conn.close()
