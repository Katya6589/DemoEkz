from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QListWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.uic import loadUi
import sys
from pages.db import connect_db
from pages.PartnersView import PartnersView

class MainWindow(QDialog):

    def __init__(self):
        """
        Создаём PartnersView, передаём весь self и cursor.
        """
        super(MainWindow, self).__init__()
        loadUi("views/dialog.ui", self)
        self.conn, self.cursor = connect_db()
        self.btnBack.clicked.connect(self.go_back) #btnBack - кнопка назад на главном окне go_back - функция ниже 
        self.btnBack.hide()
        self.stackedWidget.currentChanged.connect(self.hiddenButton)

        self.partners_view = PartnersView(self, self.cursor)
        self.partners_view.load_partners()

    def go_back(self):
        self.stackedWidget.setCurrentWidget(self.Partners)  #pagePartners - название странице где вывояься партнеры
    
    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Partners:
            self.btnBack.hide() #btnBack - кнопка назад на главном окне 
        else:
            self.btnBack.show() #btnBack - кнопка назад на главном окне 
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    icon = QIcon()
    icon.addPixmap(QPixmap("search_book_open_search_locate_6178.png"), QIcon.Normal, QIcon.Off)
    app.setWindowIcon(icon)

    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Вы закрыли приложение")