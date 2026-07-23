#textfill search 
import sys
import httpx
from PyQt6.QtWidgets import QApplication, QHeaderView, QTableWidget, QTableWidgetItem

def fetchdata(url):
        response=httpx.get(url, timeout=10)
        response.raise_for_status()
        data=response.json()   
        return data 

app = QApplication(sys.argv)
# Create a table with 3 rows and 2 columns
table = QTableWidget()
table.setWindowTitle("QTableWidget Example")

# Set column headers
table.setHorizontalHeaderLabels(["Title", "Body"])
obj=fetchdata("https://jsonplaceholder.typicode.com/posts")

table.setRowCount(len(obj))
table.setColumnCount(2)

for row_index, rowdata in enumerate(obj):
        title=rowdata["title"]
        body=rowdata["body"]
        table.setItem(row_index, 0, QTableWidgetItem(title))
        table.setItem(row_index, 1, QTableWidgetItem(body))

table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)        
# Populate data
# table.setItem(0, 0, QTableWidgetItem("Alice"))
# table.setItem(0, 1, QTableWidgetItem("25"))
# table.setItem(1, 0, QTableWidgetItem("Bob"))
# table.setItem(1, 1, QTableWidgetItem("30"))
# table.setItem(2, 0, QTableWidgetItem("Charlie"))
# table.setItem(2, 1, QTableWidgetItem("35"))

table.resize(700, 700)
table.show()

sys.exit(app.exec())
