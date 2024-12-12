from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # ...

    def scrapeAndSortData(self):
        url = "https://example.com"  # replace with the URL you want to scrape
        data = scrapeData(url)
        algorithms = [quicksort, sorted]  # add more algorithms as needed

        # Create a QTableWidget to display the data
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Data"))

        for i, item in enumerate(data):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(item))

        for algorithm in algorithms:
            sorted_data = sortAndNoteTime(data, algorithm)
            print(sorted_data)

            # Update the table with the sorted data
            for i, item in enumerate(sorted_data):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(item))

        # Add the table to the layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)