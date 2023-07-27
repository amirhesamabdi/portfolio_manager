import json
from prettytable import PrettyTable
import matplotlib.pyplot as plt

class Stock:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

class PortfolioManager:
    def __init__(self):
        self.portfolio = {}
        self.load_portfolio()

    def add_stock(self, stock):
        self.portfolio[stock.name] = stock
        self.save_portfolio()
        print("Stock added to the portfolio.")

    def update_stock_price(self, name, new_price):
        if name in self.portfolio:
            self.portfolio[name].price = new_price
            self.save_portfolio()
        else:
            print(f"Stock '{name}' not found in the portfolio.")

    def update_stock_count(self, name, new_count):
        if name in self.portfolio:
            self.portfolio[name].count = new_count
            self.save_portfolio()
        else:
            print(f"Stock '{name}' not found in the portfolio.")

    def delete_stock(self, name):
        if name in self.portfolio:
            del self.portfolio[name]
            self.save_portfolio()
            print(f"Stock '{name}' deleted from the portfolio.")
        else:
            print(f"Stock '{name}' not found in the portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("The portfolio is empty.")
            return

        total_value = sum(stock.price * stock.count for stock in self.portfolio.values())

        if total_value > 0:
            table = PrettyTable()
            table.field_names = ["Name", "Count", "Price", "Value"]

            for name, stock in self.portfolio.items():
                value = stock.price * stock.count
                table.add_row([stock.name, stock.count, f"{stock.price:.2f}", f"{value:.2f}"])

            table.add_row(["Total", "", "", f"{total_value:.2f}"])
            print(table)

            self.plot_pie_chart()
        else:
            print("The portfolio is empty or has zero value.")

    def reset_portfolio(self):
        confirm_reset = input("Are you sure you want to reset the portfolio? (yes/no): ")
        if confirm_reset.lower() == "yes":
            self.portfolio.clear()
            self.save_portfolio()
            print("Portfolio has been reset. All stocks removed.")
        else:
            print("Reset canceled. Portfolio was not changed.")

    def plot_pie_chart(self):
        labels = []
        sizes = []
        for name, stock in self.portfolio.items():
            labels.append(stock.name)
            value = stock.price * stock.count
            sizes.append(value)

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
        plt.title("Portfolio Composition")
        plt.show()

    def load_portfolio(self):
        try:
            with open("portfolio.json", "r") as file:
                data = json.load(file)
                for stock_data in data:
                    stock = Stock(stock_data["name"], stock_data["price"], stock_data["count"])
                    self.portfolio[stock.name] = stock
        except FileNotFoundError:
            pass

    def save_portfolio(self):
        data = [{"name": stock.name, "price": stock.price, "count": stock.count} for stock in self.portfolio.values()]
        with open("portfolio.json", "w") as file:
            json.dump(data, file)

def show_developer_info():
    print("\n===== App Developer Info =====")
    print("Name: Amirhesam Abdi")
    print("Email: amirhesamabdi@gmail.com")
    print("Website: https://github.com/amirhesamabdi \n")

def main():
    portfolio_manager = PortfolioManager()

    while True:
        print("\n===== Portfolio Management App =====")
        print("1. Add Stock")
        print("2. Update Stock Price")
        print("3. Update Stock Count")
        print("4. Delete Stock")
        print("5. View Portfolio")
        print("6. Reset Portfolio")
        print("7. App Developer Info")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            name = input("Enter stock name: ")
            price = float(input("Enter stock price: "))
            count = int(input("Enter stock count: "))
            stock = Stock(name, price, count)
            portfolio_manager.add_stock(stock)

        elif choice == "2":
            name = input("Enter stock name: ")
            new_price = float(input("Enter new stock price: "))
            portfolio_manager.update_stock_price(name, new_price)

        elif choice == "3":
            name = input("Enter stock name: ")
            new_count = int(input("Enter new stock count: "))
            portfolio_manager.update_stock_count(name, new_count)

        elif choice == "4":
            name = input("Enter stock name: ")
            portfolio_manager.delete_stock(name)

        elif choice == "5":
            portfolio_manager.view_portfolio()

        elif choice == "6":
            portfolio_manager.reset_portfolio()

        elif choice == "7":
            show_developer_info()

        elif choice == "8":
            print("Exiting the Portfolio Management App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
