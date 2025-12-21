from flask import Flask, redirect, render_template, request
import uuid
import json

app = Flask(__name__)

expenses = []
income= []

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        amount = float(request.form["amount"])
        type_ = request.form["type"]

        if type_ == "Income":
            categoryIn = request.form["categoryIncome"]
            id_ = str(uuid.uuid4())
            income.append({"id": id_, "name": name, "amount": amount, "type": type_, "category": categoryIn})
        else:
            categoryOut = request.form["categoryExpense"]
            id_ = str(uuid.uuid4())
            expenses.append({"id": id_, "name": name, "amount": amount, "type": type_, "category": categoryOut})

        return redirect("/")

    total_income = sum(e["amount"] for e in income)
    total_expense = sum(e["amount"] for e in expenses)

    categories = {}
    categories1 = {}
    for e in expenses:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]

    for i in income:
        cat1 = i["category"]
        categories1[cat1] = categories1.get(cat1, 0) + i["amount"]

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

@app.route("/delete/<id_>")
def delete(id_):
    global expenses, income
    expenses = [e for e in expenses if e["id"] != id_]
    income = [i for i in income if i["id"] != id_]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
