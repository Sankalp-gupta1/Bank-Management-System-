 
# 🏦 Banking Transaction Manager (with Rollback Simulation)

A web-based Banking Transaction Manager built with Flask and MySQL. Implements transaction handling using START TRANSACTION, COMMIT, and ROLLBACK to ensure safe money transfers. Features balance checks, logging, and rollback on failure. Demonstrates real-world use of stored procedures and ACID principles.

---

## 📌 Features

- 💳 Simulate secure money transfers between accounts
- ✅ Balance check before transactions
- 🔄 Auto rollback on insufficient balance or failure
- 🧾 Logs each transaction (Success/Failed)
- 🌐 Clean web interface using Flask & HTML

---

## 🧠 Concepts Used

- MySQL Transactions (`START TRANSACTION`, `COMMIT`, `ROLLBACK`)
- Stored Procedures
- ACID Properties (Atomicity, Consistency)
- Conditional Logic with IF/ELSE
- Transaction Logging
- Flask Web Integration

---

## 🛠️ Tech Stack

| Layer         | Technology      |
|---------------|-----------------|
| Backend       | Python Flask     |
| Database      | MySQL            |
| Frontend      | HTML, CSS        |
| Connector     | `mysql-connector-python` |
