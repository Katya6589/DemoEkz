from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidgetItem
)
from PyQt5.uic import loadUi
import sqlite3

class NeAvtorizovan (QDialog):
    def __init__(self, table):
        super(NeAvtorizovan, self).__init__()
        self.tableWidget_NeAvtorizovan = table 
        self.vivod()

    def vivod(self):
        conn = sqlite3.connect("BD/Knizni_club.db") 
        cur = conn.cursor()
        
        zayavki = cur.execute(f'''select 
        t.ID as "Номер товара",
        t.Naimenovanie as "Наименование",
        t.Opisanie as "Описание",
        p.Name as "Производитель",
        t.Price as "Цена",
        t.Sale as "Скидка",
        t.Photo as "Фото"
        from 
        tovar t
        LEFT JOIN
        Proisvoditel p on t.id_Proisvoditel = p.ID''')

        name_stolba = [xz[0] for xz in zayavki.description] 
        print(name_stolba)

        self.tableWidget_NeAvtorizovan.setColumnCount(len(name_stolba)) 
        self.tableWidget_NeAvtorizovan.setHorizontalHeaderLabels(name_stolba) 

        dan_table= cur.fetchall()
        
        self.tableWidget_NeAvtorizovan.setRowCount(0) 
        # row - строки
        for i, row in enumerate(dan_table): #цикл по строкам
            self.tableWidget_NeAvtorizovan.setRowCount(self.tableWidget_NeAvtorizovan.rowCount() + 1) 
            for l, cow in enumerate(row): #начинает по ячейке заносить данные
                self.tableWidget_NeAvtorizovan.setItem(i,l,QTableWidgetItem(str(cow))) 
        print(dan_table)

        self.tableWidget_NeAvtorizovan.resizeColumnsToContents() 
        conn.commit()
        conn.close()