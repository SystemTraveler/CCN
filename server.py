from flask import Flask, request, jsonify
import sqlite3
import secrets

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('wallet.db')
    conn.row_factory = sqlite3.Row
    return conn

def generate_secret_key():
    return secrets.token_urlsafe(32)

def generate_open_key():
    return secrets.token_hex(16)

def generate_mnemonic_phrase():
    words = ["abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract", "absurd", "academy", "access", "accuse", "acid", "across", "act", "action", "actor", "actress", "add", "address"]
    return ' '.join(secrets.choice(words) for _ in range(12))

@app.route('/create_wallet', methods=['POST'])
def create_wallet():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Генерация ключей и мнемонической фразы
        wallet = generate_open_key()
        secret_key = generate_secret_key()
        mnemonic_phrase = generate_mnemonic_phrase()
        
        # Проверка на уникальность кошелька
        cursor.execute('SELECT * FROM wallets WHERE wallet = ?', (wallet,))
        if cursor.fetchone():
            conn.close()
            return jsonify({'status': 'failed', 'message': 'Wallet already exists'}), 400
        
        # Вставка нового кошелька в базу данных
        cursor.execute('INSERT INTO wallets (wallet, balance, secret_key, mnemonic_phrase) VALUES (?, ?, ?, ?)', 
                       (wallet, 0, secret_key, mnemonic_phrase))
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'status': 'success',
            'wallet': wallet,
            'secret_key': secret_key,
            'mnemonic_phrase': mnemonic_phrase
        })
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500

@app.route('/balance', methods=['GET'])
def balance():
    try:
        wallet = request.args.get('Wallet')
        
        if not wallet:
            return jsonify({'status': 'failed', 'message': 'Wallet parameter is missing'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM wallets WHERE wallet = ?', (wallet,))
        wallet_data = cursor.fetchone()
        
        conn.close()
        
        if wallet_data:
            return jsonify({
                'status': 'success',
                'wallet': wallet_data['wallet'],
                'balance': wallet_data['balance']
            })
        else:
            return jsonify({'status': 'failed', 'message': 'Wallet not found'}), 404
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500

@app.route('/transaction', methods=['POST'])
def transaction():
    try:
        data = request.json
        wallet_from = data['Wallet']
        wallet_to = data['Recive']
        amount = float(data['Amount'])
        secret_key = data['SecretKey']
        unique_key = data['UniqueKey']
        
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM transactions WHERE unique_key = ?', (unique_key,))
        existing_transaction = cursor.fetchone()
        if existing_transaction:
            conn.close()
            return jsonify({'status': 'failed', 'message': 'Transaction already exists'}), 400
        
        cursor.execute('SELECT * FROM wallets WHERE wallet = ?', (wallet_from,))
        sender_wallet = cursor.fetchone()
        
        cursor.execute('SELECT * FROM wallets WHERE wallet = ?', (wallet_to,))
        receiver_wallet = cursor.fetchone()

        if not sender_wallet or not receiver_wallet:
            conn.close()
            return jsonify({'status': 'failed', 'message': 'Wallet not found'}), 404
        
        sender_balance = float(sender_wallet['balance'])
        if sender_balance < amount:
            conn.close()
            return jsonify({'status': 'failed', 'message': 'Insufficient funds'}), 400
        
        new_sender_balance = sender_balance - amount
        new_receiver_balance = float(receiver_wallet['balance']) + amount
        
        cursor.execute('UPDATE wallets SET balance = ? WHERE wallet = ?', (new_sender_balance, wallet_from))
        cursor.execute('UPDATE wallets SET balance = ? WHERE wallet = ?', (new_receiver_balance, wallet_to))
        cursor.execute('INSERT INTO transactions (wallet_from, wallet_to, amount, unique_key) VALUES (?, ?, ?, ?)',
                       (wallet_from, wallet_to, amount, unique_key))
        
        conn.commit()
        conn.close()
        
        return jsonify({'status': 'success', 'message': 'Transaction completed successfully'})
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
