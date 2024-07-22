# 钱包系统

这个项目是一个简单的钱包系统，具有创建钱包、检查余额和执行交易的功能。它使用 Flask 作为后端，SQLite 作为数据存储。

## 先决条件

- Python 3.x
- Flask
- SQLite

## 设置

1. **克隆仓库**：
    ```bash
    git clone https://github.com/SystemTraveler/CCN
    cd SystemTraveler/CCN
    ```

2. **安装所需的 Python 包**：
    ```bash
    pip install -r requirements.txt
    ```

3. **初始化数据库**：
    运行 `make.py` 脚本来创建 SQLite 数据库和必要的表：
    ```bash
    python make.py
    ```

4. **启动服务器**：
    使用 `server.py` 启动 Flask 服务器：
    ```bash
    python server.py
    ```

## API 接口

### 1. 创建钱包

- **接口**: `/create_wallet`
- **方法**: `POST`
- **请求体**: `{}` (空 JSON 对象)
- **响应**:
    ```json
    {
        "status": "success",
        "wallet": "<wallet_address>",
        "secret_key": "<secret_key>",
        "mnemonic_phrase": "<mnemonic_phrase>"
    }
    ```
- **描述**: 创建一个新的钱包，包含唯一的地址、秘密密钥和助记词。

### 2. 检查余额

- **接口**: `/balance`
- **方法**: `GET`
- **查询参数**: `Wallet` (字符串，必填)
- **响应**:
    ```json
    {
        "status": "success",
        "wallet": "<wallet_address>",
        "balance": <balance>
    }
    ```
- **描述**: 检索指定钱包的余额。

### 3. 执行交易

- **接口**: `/transaction`
- **方法**: `POST`
- **请求体**:
    ```json
    {
        "Wallet": "<wallet_from>",
        "Recive": "<wallet_to>",
        "Amount": <amount>,
        "SecretKey": "<secret_key>",
        "UniqueKey": "<unique_key>"
    }
    ```
- **响应**:
    ```json
    {
        "status": "success",
        "message": "Transaction completed successfully"
    }
    ```
- **描述**: 执行从一个钱包到另一个钱包的交易。

## 错误处理

- **400 Bad Request**: 请求参数或数据无效。
- **404 Not Found**: 钱包或交易未找到。
- **500 Internal Server Error**: 服务器内部错误。
