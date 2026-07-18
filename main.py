import database
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem


class StainlessApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stainless Shop POS")
        self.resize(900, 600)
        self.setup_ui()

    def setup_ui(self):
        #setup for tabs
        tabs = QTabWidget()

        self.tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()

        tabs.addTab(self.tab1, "Add Item")
        tabs.addTab(tab2, "New Sale")
        tabs.addTab(tab3, "Stock List")
        tabs.addTab(tab4, "Deliveries")
        

        #setup for tab1 adding an item
        layout1 = QVBoxLayout()

        self.name_label = QLabel("Product Unit Name:")
        self.name_input = QLineEdit()

        self.cost_label = QLabel("Product Cost:")
        self.cost_input = QLineEdit()

        self.sell_label = QLabel("Product Selling Price:")
        self.sell_input = QLineEdit()

        self.stock_label = QLabel("Stock Availabel:")
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

        # setup for tab3 for stocks
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Price", "Stock"])
        layout3 = QVBoxLayout()
        layout3.addWidget(self.table_widget)
        tab3.setLayout(layout3)
        self.load_db_to_table()



    def add_prod_to_db(self):
        try:
            name = self.name_input.text().strip()
            if not name:
                raise ValueError("Product name cannot be empty!")

            cost = float(self.cost_input.text())
            sell = float(self.sell_input.text())
            stock = int(self.stock_input.text())

            
            database.add_product(name, cost, sell, stock)
            print(f"Product: {name} that costs: {cost} and sells: {sell} with a quantity of {stock} is saved!")
            profit = sell - cost
            QMessageBox.information(self, "Success", f"Product --{name}-- added successfully with a profit of {profit}!")


            self.name_input.clear()
            self.cost_input.clear()
            self.sell_input.clear()
            self.stock_input.clear()

            #automatically reloads and adds the new item for tab3
            self.load_db_to_table()

        except ValueError as e:
            QMessageBox.warning(self, "Input Error", "Please ensure all numbers are typed correclty and fields are not empty!")


    def load_db_to_table(self):
        rows = database.fetch_stock()
        self.table_widget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(row[1])))
            self.table_widget.setItem(i, 1, QTableWidgetItem(str(row[3])))
            self.table_widget.setItem(i, 2, QTableWidgetItem(str(row[4])))


if __name__ == "__main__":
    database.initialize_db()
    app = QApplication(sys.argv)
    window = StainlessApp()
    window.show()
    sys.exit(app.exec())
