# Bank Management System

A banking transaction demo focused on safe transfers, rollback behavior and audit history.

## Live demo

**https://bank-management-sankalp.vercel.app/**

## Original backend

The original project uses:

- Flask
- MySQL
- a `bank_system` database
- a stored procedure for money transfer
- transaction logging

That implementation is still preserved inside `bank-flask/`.

## Deployed browser version

The new `web/` version makes the transaction rules easy to test without requiring a private MySQL server.

It includes:

- seeded bank accounts,
- balance display,
- source/destination validation,
- insufficient-balance checks,
- atomic debit + credit behavior,
- rollback on validation/invariant failure,
- audit history,
- browser persistence through `localStorage`,
- one-click reset.

The live page is a portfolio simulation. It is not a real banking system and does not handle real money.

## Run locally

```bash
cd web
python -m http.server 8000
```

Open `http://localhost:8000`.

## Run the original Flask + MySQL version

Follow the existing database setup in `bank-flask/`, create the required MySQL objects, and configure credentials locally. Do not commit real database passwords.

## Author

Sankalp Gupta  
GitHub: https://github.com/Sankalp-gupta1
