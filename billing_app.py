from datetime import datetime

class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

class Bill:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.total() for item in self.items)

def generate_invoice(bill):
    print("\n" + "=" * 40)
    print("INVOICE".center(40))
    print("=" * 40)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
    print(f"{'Item':<20}{'Qty':<5}{'Price':<8}{'Total':<7}")
    print("-" * 40)
    for item in bill.items:
        print(f"{item.name:<20}{item.quantity:<5}{item.price:<8.2f}{item.total():<7.2f}")
    print("-" * 40)
    print(f"{'Total:':<33}{bill.total():.2f}")
    print("=" * 40)

def main():
    bill = Bill()
    
    while True:
        print("\n1. Add item to bill")
        print("2. Generate invoice")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity (default 1): ") or "1")
                item = Item(name, price, quantity)
                bill.add_item(item)
                print(f"{item.name} added to the bill.")
            except ValueError:
                print("Invalid input. Please enter numeric values for price and quantity.")
        elif choice == '2':
            if bill.items:
                generate_invoice(bill)
            else:
                print("The bill is empty. Add some items first.")
        elif choice == '3':
            print("Thank you for using the billing application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()