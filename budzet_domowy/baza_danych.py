import sqlite3
import pandas as pd

DB_NAME = 'budzet.db'

def init_db():
    # Łączenie z bazą danych
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Tworzenie tabeli
    c.execute('''
        CREATE TABLE IF NOT EXISTS transakcje (
            id INTEGER PRIMARY KEY,
            data TEXT,
            opis TEXT,
            kwota REAL,
            kategoria TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Dodawanie danych
def insert_transaction(data, opis, kwota, kategoria):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO transakcje (data, opis, kwota, kategoria) VALUES (?, ?, ?, ?)",
              (data, opis, kwota, kategoria))
    conn.commit()
    conn.close()

# Pobranie danych
def get_transactions():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM transakcje", conn, parse_dates=['data'])
    conn.close()
    return df
