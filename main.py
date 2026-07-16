import database
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


    def add_prod_to_db(self):
        name = self.name_input.text()
        cost = float(self.cost_input.text())
        sell = float(self.sell_input.text())
        stock = int(self.stock_input.text())


app = QApplication(sys.argv)
window = StainlessApp()
window.show()
sys.exit(app.exec())
