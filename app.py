# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/transactions', methods=['GET'])
def list_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        new_id = len(transactions) + 1
        date = request.form['date']
        amount = float(request.form['amount'])
        new_transaction = {'id': new_id, 'date': date, 'amount': amount}
        transactions.append(new_transaction)
        return redirect(url_for('list_transactions'))

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    if request.method == 'GET':
        return render_template('edit.html', transaction=transaction)
    elif request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])
        transaction['date'] = date
        transaction['amount'] = amount
        return redirect(url_for('list_transactions'))
    return {"message": "Transaction not found"}, 404    

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    global transactions
    transactions = [t for t in transactions if t['id'] != transaction_id]
    return redirect(url_for('list_transactions'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
