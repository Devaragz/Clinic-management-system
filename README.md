# Dental Clinic Management System 🦷

A secure, modular Command Line Interface (CLI) application designed to manage dental clinic operations. This project demonstrates backend architecture principles, secure credential management, and efficient Database Management System (DBMS) integration.

## 🚀 Features
* **Modular Architecture:** Separation of concerns across database connections, authentication, and CRUD operations for scalability and maintainability.
* **Secure Authentication:** Implements `bcrypt` for cryptographic password hashing, ensuring sensitive user data is never stored in plaintext.
* **Environment Variable Management:** Utilizes `python-dotenv` to isolate and secure database credentials.
* **Automated Schema Initialization:** Dynamically sets up the MySQL database and required tables upon the first execution.
* **Comprehensive CRUD Operations:** Complete management of patient records and employee salary logs.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Database:** MySQL
* **Libraries:** `mysql-connector-python`, `bcrypt`, `python-dotenv`

## 📁 Project Structure
```text
├── main.py           # Application entry point and menu routing
├── database.py       # DB connection pool and dynamic schema setup
├── auth.py           # Bcrypt hashing and access control logic
├── operations.py     # Patient and employee CRUD execution
├── .gitignore        # Security exclusions
└── .env.example      # Template for environment variables
