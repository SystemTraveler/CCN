# Wallet System

This project is a simple wallet system with functionalities to create wallets, check balances, and execute transactions. It uses Flask for the backend and SQLite for data storage.

## Prerequisites

- Python 3.x
- Flask
- SQLite

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SystemTraveler/CCN
    cd SystemTraveler/CCN
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Initialize the database**:
    Run the `make.py` script to create the SQLite database and necessary tables:
    ```bash
    python make.py
    ```

4. **Run the server**:
    Start the Flask server using `server.py`:
    ```bash
    python server.py
    ```

## API Endpoints

### 1. Create Wallet

- **Endpoint**: `/create_wallet`
- **Method**: `POST`
- **Request Body**: `{}` (Empty JSON object)
- **Response**:
    ```json
    {
        "status": "success",
        "wallet": "<wallet_address>",
        "secret_key": "<secret_key>",
        "mnemonic_phrase": "<mnemonic_phrase>"
    }
    ```
- **Description**: Creates a new wallet with a unique address, secret key, and mnemonic phrase.

### 2. Check Balance

- **Endpoint**: `/balance`
- **Method**: `GET`
- **Query Parameters**: `Wallet` (string, required)
- **Response**:
    ```json
    {
        "status": "success",
        "wallet": "<wallet_address>",
        "balance": <balance>
    }
    ```
- **Description**: Retrieves the balance of the specified wallet.

### 3. Make a Transaction

- **Endpoint**: `/transaction`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "Wallet": "<wallet_from>",
        "Recive": "<wallet_to>",
        "Amount": <amount>,
        "SecretKey": "<secret_key>",
        "UniqueKey": "<unique_key>"
    }
    ```
- **Response**:
    ```json
    {
        "status": "success",
        "message": "Transaction completed successfully"
    }
    ```
- **Description**: Performs a transaction from one wallet to another.

## Error Handling

- **400 Bad Request**: Invalid request parameters or data.
- **404 Not Found**: Wallet or transaction not found.
- **500 Internal Server Error**: Unexpected server errors.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
