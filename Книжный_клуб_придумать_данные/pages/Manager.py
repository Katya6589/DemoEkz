from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidgetItem
)
from PyQt5.uic import loadUi
import sqlite3

class Manager (QDialog):
    def __init__(self, table):
        super(Manager, self).__init__()
        self.tableWidget_Manager = table 
        self.vivod()

    def vivod(self):
        conn = sqlite3.connect("BD/Knizni_club.db") 
        cur = conn.cursor()
        
        zayavki = cur.execute(f'''SELECT  
        t.ID as "Номер заказа", 
        t.Date_zakaza as "Дата заказа",
        tov.Naimenovanie as "Наименование товара",
        t.Sum as "Сумма товаров",
        t.Sum_Sale as "Сумма скидки",
        t.Itog_price as "Итоговая сумма",
        t.Code_polycheniya as "Код получения",
        p.Adress as "Пункт выдачи",
        ter.Adress as "Адрес терминалa",
        termin.Name_TC as "ТЦ Терминала",
        k.FIO as "ФИО клиента"
        FROM Talon t

        LEFT JOIN
        Sostav_tovara s on t.id_Sostav_tovara = s.ID_code
        LEFT JOIN
        Tovar tov on s.id_tovara = tov.ID

        left join 
        Pyntk_vidachi p on t.id_Pynkt_vidachi = p.ID
        left JOIN
        Terminal ter on t.Id_Terminal = ter.ID
        LEFT JOIN
        Terminal termin on t.Id_Terminal = termin.ID
        LEFT JOIN
        Klient k on t.id_Klient = k.ID''')

        name_stolba = [xz[0] for xz in zayavki.description] 
        print(name_stolba)

        self.tableWidget_Manager.setColumnCount(len(name_stolba)) 
        self.tableWidget_Manager.setHorizontalHeaderLabels(name_stolba) 

        dan_table= cur.fetchall()
        
        self.tableWidget_Manager.setRowCount(0) 
        # row - строки
        for i, row in enumerate(dan_table): #цикл по строкам
            self.tableWidget_Manager.setRowCount(self.tableWidget_Manager.rowCount() + 1) 
            for l, cow in enumerate(row): #начинает по ячейке заносить данные
                self.tableWidget_Manager.setItem(i,l,QTableWidgetItem(str(cow))) 
        print(dan_table)

        self.tableWidget_Manager.resizeColumnsToContents() 
        conn.commit()
        conn.close()