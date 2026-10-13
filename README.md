# Bank Management System — Transaction Lab

A banking transaction project focused on safe transfers, rollback behavior and audit history.

## Live demo

**https://bank-transaction-lab.vercel.app/**

The public demo is a browser-based transaction sandbox.

It does not use real money or a real banking database.

## What the live demo shows

- seeded accounts,
- account balances,
- transfer validation,
- insufficient-balance checks,
- atomic debit + credit behavior,
- rollback if validation fails,
- transaction history,
- local browser persistence,
- reset to the original demo state.

## Original backend

The original project is still preserved under the Flask/MySQL files.

It uses:

- Flask
- MySQL
- a `bank_system` database
- stored procedures
- transaction logging
- database transaction concepts.

The original backend is the reference for the database/ACID architecture.

## Why the hosted demo does not use MySQL

A public MySQL database would require database credentials and a persistent hosted database.

The browser simulator makes the transfer rules immediately testable without exposing a database password.

It is a portfolio simulation, not a real financial system.

## Run the live-style demo locally

```bash
cd web
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

## Run the original Flask + MySQL version

1. Install Flask and the MySQL connector.
2. Create the `bank_system` database.
3. Create the required tables and stored procedure.
4. Configure the database connection locally.
5. Start the Flask application.

Do not commit a real database password to GitHub.

## Tech stack

### Hosted demo
- HTML
- CSS
- JavaScript
- localStorage
- Vercel

### Original backend
- Python
- Flask
- MySQL
- Stored Procedures

## Author

**Sankalp Gupta**

- GitHub: https://github.com/Sankalp-gupta1
- LinkedIn: https://www.linkedin.com/in/sankalp-gupta-rishi-8617302b0/
