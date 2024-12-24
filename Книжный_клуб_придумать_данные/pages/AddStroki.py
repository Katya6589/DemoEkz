from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog
)
from PyQt5.uic import loadUi
import sqlite3

class AddStroki (QDialog):
    def __init__(self):
        super(AddStroki, self).__init__()