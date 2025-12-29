# Budget Web App - HTML file

This folder contains all HTML templates for the Budget App. These templates are dynamically rendered by Flask using the Jinja2 templating engine.

---

## Contents
- index.html : Main template for the app. Handles:
  - Displaying the form to add income and expenses
  - Showing total income, total expenses and net balance
  - Listing entries for income and expenses
  - Showing category-wise breakdowns
  - Displaying charts using Chart.js
  - Contains JavaScript

---

## Notes
- Templates use Jinja2 syntax to dynamically insert data from the Flask backend.
- All templates stored in this folder allow Flask to find and render them.
- Template files reference static assets (CSS) via url_for('static', filename='...').
