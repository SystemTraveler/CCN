import sqlite3

def initialize_db():
    conn = sqlite3.connect('Wallet.db')
    cursor = conn.cursor()
    
    # Удалите таблицу, если она существует
    cursor.execute('DROP TABLE IF EXISTS wallets')
    
    # Создайте таблицу с нужной схемой
    cursor.execute('''
        CREATE TABLE wallets (
            wallet TEXT PRIMARY KEY,
            balance REAL,
            secret_key TEXT,
            mnemonic_phrase TEXT
        )
    ''')
    
    # Создайте таблицу для транзакций, если нужно
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet_from TEXT,
            wallet_to TEXT,
            amount REAL,
            unique_key TEXT UNIQUE
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
