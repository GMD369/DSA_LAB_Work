class CashFlowMinimizer:
    def __init__(self):
        self.transactions = []  # List of (borrower, lender, amount)
        self.balances = {}

    def add_transaction(self, from_person, to_person, amount):
        self.transactions.append((from_person, to_person, amount))
        self.balances[from_person] = self.balances.get(from_person, 0) - amount
        self.balances[to_person] = self.balances.get(to_person, 0) + amount

    def minimize_cash_flow(self):
        # Step 1: Separate debtors and creditors
        debtors = []
        creditors = []
        for person, balance in self.balances.items():
            if balance < 0:
                debtors.append((person, abs(balance)))
            elif balance > 0:
                creditors.append((person, balance))

        # Step 2: Match debtors with creditors
        transactions_to_settle = []
        i, j = 0, 0
        while i < len(debtors) and j < len(creditors):
            debtor, debt = debtors[i]
            creditor, credit = creditors[j]

            transfer_amount = min(debt, credit)
            transactions_to_settle.append((debtor, creditor, transfer_amount))

            # Update balances
            debtors[i] = (debtor, debt - transfer_amount)
            creditors[j] = (creditor, credit - transfer_amount)

            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1

        return transactions_to_settle

    def display_transactions(self, transactions_to_settle):
        print("\nSimplified Transactions:")
        for transaction in transactions_to_settle:
            print(f"{transaction[0]} owes {transaction[1]}: {transaction[2]} units.")

    def input_transactions(self):
        print("Enter transactions in the format: FromPerson ToPerson Amount")
        print("Type 'done' when finished.")

        while True:
            user_input = input("Transaction: ")
            if user_input.lower() == 'done':
                break

            try:
                from_person, to_person, amount = user_input.split()
                amount = float(amount)
                self.add_transaction(from_person, to_person, amount)
            except ValueError:
                print("Invalid input format. Please try again.")

# Example usage:
if __name__ == "__main__":
    cfm = CashFlowMinimizer()
    cfm.input_transactions()

    transactions_to_settle = cfm.minimize_cash_flow()
    cfm.display_transactions(transactions_to_settle)