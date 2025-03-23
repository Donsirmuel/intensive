from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Initialize data
data = pd.DataFrame(columns=['User', 'Date', 'Income', 'Expenses', 'Savings', 'Comments'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['user']
        date = request.form['date']
        income = (request.form['income'])
        expenses = (request.form['expenses'])
        savings = (request.form['savings'])
        comments = (request.form['comments'])
        new_row = pd.DataFrame([[user, date, income, expenses, savings, comments]], columns=['User', 'Date', 'Income', 'Expenses', 'Savings', 'Comments'])
        global data
        data = pd.concat([data, new_row], ignore_index=True)
        data.to_csv('finance_data.csv', index=False)
    return render_template('index.html', data=data.to_html())

if __name__ == "__main__":
    app.run(debug=True)