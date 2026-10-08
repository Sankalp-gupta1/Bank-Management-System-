# Banking Transaction Manager

A Flask + MySQL banking transaction demo focused on **safe money transfers, rollback behavior, transaction logging, and ACID-style database concepts**.

## Overview

The application displays bank accounts and transaction history through a web interface and delegates money transfers to a MySQL stored procedure.

The transfer flow is designed around:

- balance validation
- transactional updates
- commit on success
- rollback on failure
- transaction logging

## Features

- Transfer money between accounts
- View account records
- View transaction logs
- Commit successful transactions
- Roll back failed transfers
- Stored-procedure based transfer flow
- Flask web interface

## Tech Stack

- Python
- Flask
- MySQL
- mysql-connector-python
- HTML / CSS

## Concepts Demonstrated

- ACID properties
- Database transactions
- `COMMIT`
- `ROLLBACK`
- Stored procedures
- Transaction logging
- Error handling between Flask and MySQL

## Project Structure

```text
Bank-Management-System-/
├── bank-flask/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── project documentation
├── dbms_monitor/
├── privileges_monitor/
└── README.md
```

## Prerequisites

- Python 3
- MySQL Server
- A MySQL database named `bank_system`
- Required `accounts`, `transaction_log`, and `transfer_money` database objects

## Installation

Clone the repository:

```bash
git clone https://github.com/Sankalp-gupta1/Bank-Management-System-.git
cd Bank-Management-System-/bank-flask
```

Install Python dependencies:

```bash
pip install flask mysql-connector-python
```

## Database Configuration

The Flask app currently connects to a local MySQL server.

Before running it:

1. Create/configure the `bank_system` database.
2. Make sure the required tables and `transfer_money` stored procedure exist.
3. Update the MySQL connection settings in `bank-flask/app.py` for your local environment.
4. Do not commit real database passwords to a public repository.

## Run

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Transaction Flow

```text
User submits transfer
        │
        ▼
Flask calls transfer_money(...)
        │
        ├── success → COMMIT
        │
        └── error   → ROLLBACK
        │
        ▼
Accounts + transaction log refreshed
```

## Screenshots

![Banking UI](https://github.com/user-attachments/assets/baf00222-4923-4cfd-81c3-7c1fbe3b8655)

![Transaction View](https://github.com/user-attachments/assets/8103c186-099b-41a4-9394-4907509c10c5)

## Author

**Sankalp Gupta**

GitHub: https://github.com/Sankalp-gupta1
