from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidget, QMessageBox,QLabel, QPushButton, QLineEdit, QComboBox, QSpinBox
)
import sqlite3

import re
from pages.SavePartner import SavePartner


class AddPartner(QDialog):
    def __init__(self, ui, cursor):
        super(AddPartner, self).__init__()
        self.ui = ui
        self.cursor = cursor
        self.SavePartner = SavePartner(ui, cursor, inn=None)
        
        self.SavePartner.clear_inputs()
        self.SavePartner.load_types()

        self.Add_but = self.ui.findChild(QPushButton, "Add_button")
        self.Add_but.clicked.connect(self.SavePartner.save_partner)

