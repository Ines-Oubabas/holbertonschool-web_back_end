# Personal Data Project

This project demonstrates logging with PII data obfuscation, password encryption, and secure database access.

## Features

- Regex-based field redaction for logs
- Logging formatter with configurable fields
- Password hashing and validation using bcrypt
- MySQL database connection using environment variables

## Setup

1. Create a `.env` or export these variables:

export PERSONAL_DATA_DB_USERNAME=root
export PERSONAL_DATA_DB_PASSWORD=root
export PERSONAL_DATA_DB_HOST=localhost
export PERSONAL_DATA_DB_NAME=my_db


2. Run `filtered_logger.py` to see secure logs.

3. Run `main.py` to test password hashing.