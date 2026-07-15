import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton


class StainlessApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stainless Shop POS")
        self.resize(900, 600)

        self.setup_ui()

    def setup_ui(self):
        tabs = QTabWidget()

        self.tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()

        tabs.addTab(self.tab1, "Add Item")
        tabs.addTab(tab2, "New Sale")
        tabs.addTab(tab3, "Stock List")
        tabs.addTab(tab4, "Deliveries")

        layout1 = QVBoxLayout()

        self.name_label = QLabel("Product Unit Name:")
        self.name_input = QLineEdit()

        self.cost_label = QLabel("Product Cost:")
        self.cost_input = QLineEdit()

        self.sell_label = QLabel("Product Selling Price:")
        self.sell_input = QLineEdit()

        self.stock_label = QLabel("Stock Availabel:")
        self.stock_input = QLineEdit()








# app = QApplication(sys.argv)
# window = QMainWindow()

# window.setWindowTitle("Stainless Shop POS")
# window.resize(900, 700)


# tabs = QTabWidget()

# tab1 = QWidget()
# tab2 = QWidget()
# tab3 = QWidget()
# tab4 = QWidget()

# tabs.addTab(tab1, "Add Item")
# tabs.addTab(tab2, "New Sale")
# tabs.addTab(tab3, "Stock List")
# tabs.addTab(tab4, "Deliveries")



# def add_prod_to_db():
#     name = name_input.text()
#     cost = cost_input.text()
#     sell = sell_input.text()
#     stock = stock_input.text()
#     print(f"Saved! {name, cost, sell, stock}")



# layout1 = QVBoxLayout()

# name_label = QLabel("Product Unit Name:")
# name_input = QLineEdit()

# cost_label = QLabel("Product Cost:")
# cost_input = QLineEdit()

# sell_label = QLabel("Product Selling Price:")
# sell_input = QLineEdit()

# stock_label = QLabel("Stock Available:")
# stock_input = QLineEdit()

# save_button = QPushButton("Save Product")


# layout1.addWidget(name_label)
# layout1.addWidget(name_input)

# layout1.addWidget(cost_label)
# layout1.addWidget(cost_input)

# layout1.addWidget(sell_label)
# layout1.addWidget(sell_input)

# layout1.addWidget(stock_label)
# layout1.addWidget(stock_input)

# layout1.addWidget(save_button)
# save_button.clicked.connect(add_prod_to_db)


# tab1.setLayout(layout1)











# window.setCentralWidget(tabs)
# window.show()

# sys.exit(app.exec())


