from flask import Flask, redirect, render_template, request, Response
import sqlite3
import json
import os  #for testing
from datetime import datetime
import csv

app = Flask(__name__)

def get_db_name():
    return os.environ.get("DB_NAME", "budget.db")

def init_db():
    conn = sqlite3.connect(get_db_name()) #opens connection to sql database file
    c = conn.cursor()   #creates cursor to execute SQL commands

    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')

    c.execute('''
            CREATE TABLE IF NOT EXISTS income (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
        ''')

    conn.commit()
    conn.close()


def add_expense(name, amount, category):
    conn = sqlite3.connect(get_db_name())
    c = conn.cursor()
    c.execute("INSERT INTO expenses (name, amount, category, date) VALUES (?, ?, ?, ?)",
              (name, amount, category, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()


def add_income(name, amount, category):
    conn = sqlite3.connect(get_db_name())
    c = conn.cursor()
    c.execute("INSERT INTO income (name, amount, category, date) VALUES (?, ?, ?, ?)",
              (name, amount, category, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()


def get_expenses():
    conn = sqlite3.connect(get_db_name())
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")  #SQL query
    data = c.fetchall()  #Fetch all rows returned by the query
    conn.close()
    return data  #return list of rows


def get_income():
    conn = sqlite3.connect(get_db_name())
    c = conn.cursor()
    c.execute("SELECT * FROM income")
    data = c.fetchall()
    conn.close()
    return data

def delete_entry(table, entry_id):
    conn = sqlite3.connect(get_db_name())
    c = conn.cursor()
    c.execute(f"DELETE FROM {table} WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()

init_db()  #initialise DB

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        amount = float(request.form["amount"])
        type_ = request.form["type"]

        #validation
        if not name.replace(" ","").isalpha(): #spaces
            return "Invalid name!", 400

        try:
            if amount <= 0:
                return "Amount must be positive!", 400
        except ValueError:
            return "Amount must be a number!", 400

        if type_ not in ["Income", "Expense"]:
            return "Invalid type!", 400

        if type_ == "Income":
            category = request.form.get("categoryIncome")
            if category not in ["Salary", "Freelance", "Investment", "Other"]:
                return "Invalid income category!", 400
            add_income(name, amount, category)
        else:
            category = request.form.get("categoryExpense")
            if category not in ["Food", "Transport", "Bills", "Entertainment", "Other"]:
                return "Invalid expense category!", 400
            add_expense(name, amount, category)

        return redirect("/")

    expenses = get_expenses()
    income = get_income()

    total_income = sum(i[2] for i in income)
    total_expense = sum(e[2] for e in expenses)

    categories = {}
    categories1 = {}
    for e in expenses:
        categories[e[3]] = categories.get(e[3], 0) + e[2]

    for i in income:
        categories1[i[3]] = categories1.get(i[3], 0) + i[2]

    return render_template(
        "index.html",
        expenses=expenses,
        income = income,
        total_income=total_income,
        total_expense=total_expense,
        categories=categories,
        categories1= categories1,
        categories_json = json.dumps(categories),
        categories1_json = json.dumps(categories1),
        totals_json = json.dumps({
            "Income": total_income,
            "Expense": total_expense
        })
    )

@app.route("/delete/<table>/<int:entry_id>")
def delete(table, entry_id):
    if table not in ["expenses", "income"]:
        return "Invalid table!", 400
    delete_entry(table, entry_id)
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    conn = sqlite3.connect(get_db_name())
    c = conn.cursor()
    c.execute("DELETE FROM expenses")
    c.execute("DELETE FROM income")
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/export/csv")
def export_csv():
    expenses = get_expenses()
    income = get_income()

    def generate():   #Efficient for large data and streams the file like being downloaded instead of loading the whole thing in memory
        yield "type,id,name,amount,category,date\n"

        for e in expenses:
            yield f"expense,{e[0]},{e[1]},{e[2]},{e[3]},{e[4]}\n"

        for i in income:
            yield f"income,{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n"


    return Response(
        generate(),
        mimetype="text/csv", #tells browser that this is a csv file
        headers={"Content-Disposition": "attachment; filename=budget_data.csv"}
    )





if __name__ == "__main__":
    app.run(debug=True)
