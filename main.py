import database
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QLabel,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
)


class StainlessApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stainless Shop POS")
        self.resize(900, 600)
        self.setup_ui()

    def setup_ui(self):
        # setup for tabs
        tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        tabs.addTab(self.tab1, "Add Item")
        tabs.addTab(self.tab2, "New Sale")
        tabs.addTab(self.tab3, "Stock List")
        tabs.addTab(self.tab4, "Deliveries")

        # setup for tab1 adding an item
        layout1 = QVBoxLayout()

        self.name_label = QLabel("Product Unit Name:")
        self.name_input = QLineEdit()

        self.cost_label = QLabel("Product Cost:")
        self.cost_input = QLineEdit()

        self.sell_label = QLabel("Product Selling Price:")
        self.sell_input = QLineEdit()

        self.stock_label = QLabel("Stock Available:")
        self.stock_input = QLineEdit()

        save_button = QPushButton("Save Product")

        layout1.addWidget(self.name_label)
        layout1.addWidget(self.name_input)
        layout1.addWidget(self.cost_label)
        layout1.addWidget(self.cost_input)
        layout1.addWidget(self.sell_label)
        layout1.addWidget(self.sell_input)
        layout1.addWidget(self.stock_label)
        layout1.addWidget(self.stock_input)
        layout1.addWidget(save_button)

        save_button.clicked.connect(self.add_prod_to_db)

        self.tab1.setLayout(layout1)
        self.setCentralWidget(tabs)

        # setup for tab2 for new sale
        self.dropdown = QComboBox()
        layout2 = QVBoxLayout()
        self.name_label = QLabel("Products:")

        self.stock_display_label = QLabel("Available stock: 0")

        self.price_display_label = QLabel("Price:")
        self.price_display_input = QLineEdit()

        self.sold_to_label = QLabel("Sold to:")
        self.sold_to = QLineEdit()
        self.sold_to.setPlaceholderText("Enter name...")

        self.save_new_sale = QPushButton("Add Sale")

        self.cost = QLabel("Unit Cost: 0")

        self.sale_quantity_label = QLabel("Quantity:")
        self.sale_quantity = QLineEdit()

        self.save_new_sale.clicked.connect(self.new_sale)

        self.sale_prod_names_update()
        self.dropdown.currentTextChanged.connect(self.get_dropdown_data)
        self.get_dropdown_data()

        layout2.addWidget(self.name_label)
        layout2.addWidget(self.dropdown)
        layout2.addWidget(self.stock_display_label)
        layout2.addWidget(self.cost)
        layout2.addWidget(self.price_display_label)
        layout2.addWidget(self.price_display_input)
        layout2.addWidget(self.sale_quantity_label)
        layout2.addWidget(self.sale_quantity)
        layout2.addWidget(self.sold_to_label)
        layout2.addWidget(self.sold_to)
        layout2.addWidget(self.save_new_sale)
        self.tab2.setLayout(layout2)

        # setup for tab3 for stocks
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Price", "Stock"])
        layout3 = QVBoxLayout()

        # adding reset button
        reset_butt = QPushButton("Reset Database")
        reset_butt.clicked.connect(self.delete_db)

        layout3.addWidget(reset_butt)
        layout3.addWidget(self.table_widget)
        self.tab3.setLayout(layout3)
        self.load_db_to_table()

    # saves product to database
    def add_prod_to_db(self):
        try:
            name = self.name_input.text().strip()
            # checks if "name" is empty
            if not name:
                raise ValueError("Product name cannot be empty!")
            # checks if product name is or has a number
            if any(char.isdigit() for char in name):
                raise ValueError("Product name must not have any numbers!")

            # check "cost" if empty
            if not self.cost_input.text().strip():
                raise ValueError("Product cost cannot be empty!")
            # checks if it is a float
            try:
                cost = float(self.cost_input.text())
            except:
                raise ValueError("Product cost must be a number!")
            # check if less than or equal to zero

            if cost <= 0:
                raise ValueError("Product cost must be greater than zero!")

            # checks if sell is empty
            if not self.sell_input.text().strip():
                raise ValueError("Selling price cannot be empty!")
            try:
                sell = float(self.sell_input.text())
            except:
                raise ValueError("Selling price must be a number!")
            # checks if sell is less than or equal to zero
            if sell <= 0:
                raise ValueError("Selling price must be greater than zero!")

            # checks if stock input is empty
            if not self.stock_input.text().strip():
                raise ValueError("Stock cannot be empty!")
            try:
                stock = int(self.stock_input.text())
            except:
                raise ValueError("Stock must be a number!")
            # checks if stock is less than zero
            if stock < 0:
                raise ValueError("Product stock cannot be less than zero!")

            database.add_product(name, cost, sell, stock)
            print(
                f"Product: {name} that costs: {cost} and sells: {sell} with a quantity of {stock} is saved!"
            )
            profit = sell - cost
            QMessageBox.information(
                self,
                "Success",
                f"Product --{name}-- added successfully with a profit of {profit}!",
            )

            # updates the dropdown options in tab2 for new sale
            self.sale_prod_names_update()

            self.name_input.clear()
            self.cost_input.clear()
            self.sell_input.clear()
            self.stock_input.clear()

            # automatically reloads and adds the new item for tab3
            self.load_db_to_table()

        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))

    def load_db_to_table(self):
        rows = database.fetch()
        self.table_widget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(row[1])))
            self.table_widget.setItem(i, 1, QTableWidgetItem(str(row[3])))
            self.table_widget.setItem(i, 2, QTableWidgetItem(str(row[4])))

    # prod names
    def sale_prod_names_update(self):
        prod_names = database.fetch_prod_names()
        self.dropdown.clear()
        self.dropdown.addItems(prod_names)

    # gets the product data
    def get_dropdown_data(self):
        selected_prod_name = self.dropdown.currentText()
        prod_data = database.fetch_prod_by_name(selected_prod_name)

        if prod_data:
            prod_id = prod_data[0]
            price = prod_data[1]
            stock = prod_data[2]
            cost = prod_data[3]
            self.stock_display_label.setText(f"Available stock: {stock}")
            self.price_display_input.setPlaceholderText(str(price))
            self.cost.setText(f"Unit Cost: {cost}")
            self.prod_id = prod_id

    # deletes the whole database for products
    def delete_db(self):
        delete_confirmation = QMessageBox.question(
            self,
            "WARNING",
            "Are you sure you want to delete all database?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if delete_confirmation == QMessageBox.StandardButton.Yes:
            database.delete_db()

            self.load_db_to_table()
            self.sale_prod_names_update()

            QMessageBox.information(self, "Success", "The database has been reset.")

    def new_sale(self):
        try:
            id = self.prod_id
            # prod = self.dropdown.currentText()

            price_text = self.price_display_input.text().strip()
            if not price_text:
                price_text = self.price_display_input.placeholderText()

            try:
                price = float(price_text)
            except:
                raise ValueError("Product price must be a number!")

            quantity_text = self.sale_quantity.text().strip()
            if not quantity_text:
                raise ValueError("Product quantity must not be empty!")

            try:
                quantity = int(quantity_text)
            except:
                raise ValueError("Product quantity must be a number!")

            cost_text = self.cost.text().replace("Unit Cost: ", "").strip()
            if not cost_text:
                raise ValueError("Product cost cannot be empty!")

            try:
                cost = float(cost_text)
            except:
                raise ValueError("Product cost must be a number!")

            sold = self.sold_to.text().strip()
            if not sold:
                raise ValueError("Customer name must not be empty!")

            # stock = self.stock _display_label

            # gets the available stock then gets the text replaces the text with nothing then strips whitespaces
            stock_int = int(
                self.stock_display_label.text().replace("Available stock: ", "").strip()
            )

            # gets the actual stock by deducting the bought quantity
            stock = stock_int - quantity

            # calls the function for updating the stock inside the database
            database.update_product_stock(id, stock)

            database.new_sale(id, sold, quantity, cost, price)

            self.sold_to.clear()
            self.sale_quantity.clear()
            self.price_display_input.clear()

            # updates the stock when adding a new sale once button hits
            self.get_dropdown_data()

            # sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            # product_id INTEGER,
            # sold_to TEXT NOT NULL,
            # sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            # sale_quantity INTEGER NOT NULL,
            # unit_cost REAL NOT NULL,
            # selling_price REAL NOT NULL
        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))


if __name__ == "__main__":
    database.initialize_db()
    app = QApplication(sys.argv)
    window = StainlessApp()
    window.show()
    sys.exit(app.exec())
