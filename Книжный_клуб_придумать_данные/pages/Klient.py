from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidgetItem
)
from PyQt5.uic import loadUi
import sqlite3


class Klient (QDialog):
    def __init__(self, table): 
        super(Klient, self).__init__()
        self.tableWidget_Klient = table 
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

        self.tableWidget_Klient.setColumnCount(len(name_stolba)) 
        self.tableWidget_Klient.setHorizontalHeaderLabels(name_stolba) 

        dan_table= cur.fetchall()
        
        self.tableWidget_Klient.setRowCount(0) 
        # row - строки
        for i, row in enumerate(dan_table): #цикл по строкам
            self.tableWidget_Klient.setRowCount(self.tableWidget_Klient.rowCount() + 1) 
            for l, cow in enumerate(row): #начинает по ячейке заносить данные
                self.tableWidget_Klient.setItem(i,l,QTableWidgetItem(str(cow))) 
        print(dan_table)

        self.tableWidget_Klient.resizeColumnsToContents() 
        conn.commit()
        conn.close()

   

        
    
   