# Monujo Sistemo

Ĉi tiu projekto estas simpla monujo sistemo kun funkcioj por krei monujojn, kontroli ekvilibrojn kaj plenumi transakciojn. Ĝi uzas Flask por la malantaŭa servo kaj SQLite por datuma stokado.

## Postuloj

- Python 3.x
- Flask
- SQLite

## Agordo

1. **Klonu la depoziton**:
    ```bash
    git clone https://github.com/SystemTraveler/CCN
    cd SystemTraveler/CCN
    ```

2. **Instalu la bezonatajn Python-pakaĵojn**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Iniciu la datumbazon**:
    Rulu la skripton `make.py` por krei la SQLite-datumbazon kaj necesajn tabelojn:
    ```bash
    python make.py
    ```

4. **Startigu la serveron**:
    Startigu la Flask-servon uzante `server.py`:
    ```bash
    python server.py
    ```

## API Finpunktoj

### 1. Krei Monujon

- **Finpunkto**: `/create_wallet`
- **Metodo**: `POST`
- **Petaj Korpo**: `{}` (Malplena JSON objekto)
- **Respondo**:
    ```json
    {
        "status": "success",
        "wallet": "<wallet_address>",
        "secret_key": "<secret_key>",
        "mnemonic_phrase": "<mnemonic_phrase>"
    }
    ```
- **Priskribo**: Kreas novan monujon kun unika adreso, sekreta ŝlosilo kaj mnemonika frazo.

### 2. Kontroli Ekvilibron

- **Finpunkto**: `/balance`
- **Metodo**: `GET`
- **Demandoj Parametroj**: `Wallet` (stringo, necesa)
- **Respondo**:
    ```json
    {
        "status": "success",
        "wallet": "<wallet_address>",
        "balance": <balance>
    }
    ```
- **Priskribo**: Akiras la ekvilibron de la specifita monujo.

### 3. Plenumi Transakcion

- **Finpunkto**: `/transaction`
- **Metodo**: `POST`
- **Petaj Korpo**:
    ```json
    {
        "Wallet": "<wallet_from>",
        "Recive": "<wallet_to>",
        "Amount": <amount>,
        "SecretKey": "<secret_key>",
        "UniqueKey": "<unique_key>"
    }
    ```
- **Respondo**:
    ```json
    {
        "status": "success",
        "message": "Transaction completed successfully"
    }
    ```
- **Priskribo**: Plenumas transakcion de unu monujo al alia.

## Eraro Traktado

- **400 Bad Request**: Malvalidaj petaj parametroj aŭ datumoj.
- **404 Not Found**: Monujo aŭ transakcio ne trovita.
- **500 Internal Server Error**: Neatenditaj servilaj eraroj.
