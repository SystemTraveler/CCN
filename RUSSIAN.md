# Система Кошелька

Этот проект представляет собой простую систему кошельков с функциональностью создания кошельков, проверки балансов и выполнения транзакций. Использует Flask для бэкенда и SQLite для хранения данных.

## Требования

- Python 3.x
- Flask
- SQLite

## Настройка

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/SystemTraveler/CCN
    cd SystemTraveler/CCN
    ```

2. **Установите необходимые Python пакеты**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Инициализируйте базу данных**:
    Запустите скрипт `make.py`, чтобы создать базу данных SQLite и необходимые таблицы:
    ```bash
    python make.py
    ```

4. **Запустите сервер**:
    Запустите сервер Flask, используя `server.py`:
    ```bash
    python server.py
    ```

## API Эндпоинты

### 1. Создать Кошелек

- **Эндпоинт**: `/create_wallet`
- **Метод**: `POST`
- **Тело Запроса**: `{}` (Пустой JSON объект)
- **Ответ**:
    ```json
    {
        "status": "success",
        "wallet": "<wallet_address>",
        "secret_key": "<secret_key>",
        "mnemonic_phrase": "<mnemonic_phrase>"
    }
    ```
- **Описание**: Создает новый кошелек с уникальным адресом, секретным ключом и мнемонической фразой.

### 2. Проверить Баланс

- **Эндпоинт**: `/balance`
- **Метод**: `GET`
- **Параметры Запроса**: `Wallet` (строка, обязательный)
- **Ответ**:
    ```json
    {
        "status": "success",
        "wallet": "<wallet_address>",
        "balance": <balance>
    }
    ```
- **Описание**: Получает баланс указанного кошелька.

### 3. Сделать Транзакцию

- **Эндпоинт**: `/transaction`
- **Метод**: `POST`
- **Тело Запроса**:
    ```json
    {
        "Wallet": "<wallet_from>",
        "Recive": "<wallet_to>",
        "Amount": <amount>,
        "SecretKey": "<secret_key>",
        "UniqueKey": "<unique_key>"
    }
    ```
- **Ответ**:
    ```json
    {
        "status": "success",
        "message": "Transaction completed successfully"
    }
    ```
- **Описание**: Выполняет транзакцию от одного кошелька к другому.

## Обработка Ошибок

- **400 Bad Request**: Неверные параметры запроса или данные.
- **404 Not Found**: Кошелек или транзакция не найдены.
- **500 Internal Server Error**: Неожиданные ошибки сервера.
