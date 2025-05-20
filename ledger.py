import csv
import os
import argparse
import datetime

class Ledger:
    def __init__(self, filename='ledger.csv'):
        self.filename = filename
        self.records = []
        if os.path.exists(self.filename):
            with open(self.filename, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['amount'] = float(row['amount'])
                    self.records.append(row)
        else:
            with open(self.filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['date', 'type', 'amount', 'description'])
                writer.writeheader()

    def add(self, record_type, amount, description=''):
        self.records.append({
            'type': record_type,
            'amount': amount,
            'description': description,
            'date': datetime.date.today().isoformat()
        })
        self.save()

    def save(self):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['date', 'type', 'amount', 'description'])
            writer.writeheader()
            for r in self.records:
                writer.writerow(r)

    def list(self):
        return self.records

    def balance(self):
        total = 0
        for r in self.records:
            if r['type'] == 'income':
                total += r['amount']
            else:
                total -= r['amount']
        return total

def main():
    parser = argparse.ArgumentParser(description='Simple ledger software')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a record')
    add_parser.add_argument('type', choices=['income', 'expense'])
    add_parser.add_argument('amount', type=float)
    add_parser.add_argument('-d', '--description', default='')

    subparsers.add_parser('list', help='List records')
    subparsers.add_parser('balance', help='Show balance')

    args = parser.parse_args()
    ledger = Ledger()

    if args.command == 'add':
        ledger.add(args.type, args.amount, args.description)
        print('Record added.')
    elif args.command == 'list':
        for r in ledger.list():
            print(f"{r['date']} {r['type']} {r['amount']:.2f} {r['description']}")
    elif args.command == 'balance':
        print(f"Balance: {ledger.balance():.2f}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
