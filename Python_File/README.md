# Budget Web App - PROTOTYPE

This folder contains the **prototype** of the Budget Web App. 
A simple Flask-based finance tracker prototype built to explore full-stack fundamentals and basic data visualisation.

This version focuses on core functionality and using **in-memory storage** instead of integrating a database. The prototype was created to develop a understanding of Flask, JSON, Jinja, Chart.js and JavaScript along with integrating the front-end with the back-end.

---

## Features
- Add Income and Expense entries
- Categorise transactions
- View:
  - Total Income
  - Total Expense
  - Net Balance
  - Last entries
- Category-wise breakdown for income and expenses
- Delete individual entries
- Basic charts using Chart.js

---

## Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Charts: Chart.js
- Data Storage: In-memory Python lists (prototype only)

---

## Design Notes
- Each transaction is assigned a unique UUID
- Data is stored in Python lists
- All data resets when the server restarts
- Focus was on:
  - Request handling: Implemented multiple routes and handles GET/POST requests 
  - Form processing: Processed form data securely using Flask's request object and routed logic based on user input
  - Data aggregation: Combined transactional data to compute totals and category-wise summaries
  - Template rendering: Used Jinja templates to dynamically render UI components based on backend data
  - Rapid iteration: Followed an iterative development approach, continuously learning and improving functionality and UI

---

## Limitations (Known & Intentional)
- No database (Prototype only uses Python lists and data is lost on refresh/server restart)
- No server-side validation
- No CSV export
- Not production-ready
These limitations are later addressed and the prototype is improved in a later fully refactored version of the project.

---

## How to Run
1. Install dependencies:

```bash
pip install flask
```

2. Run the application:

```bash
python main.py
```

3. Then open:

http://127.0.0.1:5000

---

## Project Evolution
This repository documents the evolution of the project:
- Prototype: In-memory storage, basic CRUD
- Refactor: Database integration, data persistance, validation, CSV export, UI improvements

---

## AUTHOR

Arittri Ray
Software Engineering | Learning Flask & full-stack development
 

 







