from flask import Flask, request, redirect, url_for, render_template_string
from ledger import Ledger

app = Flask(__name__)
ledger = Ledger()

TEMPLATE = '''
<!doctype html>
<title>Ledger</title>
<h1>Ledger Records</h1>
<table border="1">
<tr><th>Date</th><th>Type</th><th>Amount</th><th>Description</th></tr>
{% for r in records %}
<tr>
  <td>{{ r['date'] }}</td>
  <td>{{ r['type'] }}</td>
  <td>{{ '%.2f'|format(r['amount']) }}</td>
  <td>{{ r['description'] }}</td>
</tr>
{% endfor %}
</table>
<h2>Balance: {{ '%.2f'|format(balance) }}</h2>
<h2>Add Record</h2>
<form method="post" action="/add">
  <select name="type">
    <option value="income">Income</option>
    <option value="expense">Expense</option>
  </select>
  <input name="amount" type="number" step="0.01" required>
  <input name="description" placeholder="Description">
  <button type="submit">Add</button>
</form>
'''

@app.route('/')
def index():
    return render_template_string(TEMPLATE, records=ledger.list(), balance=ledger.balance())

@app.route('/add', methods=['POST'])
def add_record():
    record_type = request.form['type']
    amount = float(request.form['amount'])
    description = request.form.get('description', '')
    ledger.add(record_type, amount, description)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
