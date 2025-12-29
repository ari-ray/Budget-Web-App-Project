# Budget Web App - REFACTORED FINAL VERSION

This folder contains the ***refactored finalised version*** of the Budget Web App.

A full-featured Flask-based finance tracker for managing income and expenses. This version refactors the prototype with database integration, server-side validation, CSV export, and UI improvements.

This project demonstrates building a robust full-stack web application with Python, Flask, Jinja templates, JavaScript and Chart.js.

---

## Features
- Add Income and Expense entries
- Categorize transactions
- View totals and net balance
- Category-wise breakdowns with charts (Chart.js)
- Delete individual entries
- Reset all data
- CSV export of all transactions
- Server-side validation for safer input
- Database integration for data persistance

---

## Tech Stack

- Backend: Python, Flask, SQLite
- Frontend: HTML, CSS, JavaScript, Jinja templates
- Charts: Chart.js
- Data Storage: SQLite database (budget.db)

---

## Design Notes

- Persistent storage: Transactions stored in SQLite instead of in-memory lists
- Validation: Ensures amounts are positive, names are valid, and categories match predefined options
- CSV export: Downloads all data efficiently using Flask Response
- UI & UX: Improved layout, responsive design, and user feedback on actions
- Modular structure: Separate static assets and templates for maintainability

---

## How to Run

- Install dependencies:
  
```bash
pip install flask
```

- Run the application:
  
```bash
python main2.py
```

- Open in browser:
http:// 127.0.0.1:5000

---

## Project Evolution
This refactored version is the **FINAL STAGE** of the project evolution
- Prototype: In-memory storage, basic CRUD, no validation, no CSV export
- Refactored: Database integration, persistant storage, validation, CSV export, improved UI

---

## Limitations
- Still a single user app (no authentication)
- SQLite may not scale for multiple concurrent users (production-ready would need a more robust database

---

## AUTHOR
Arittri Ray
Software Engineering | Full-stack Web Development Enthusiast







