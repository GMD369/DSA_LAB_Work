def Merge(array,p,q,r):
    leftHalf=array[p:q+1]
    rightHalf=array[q+1:r+1]
    i=0
    j=0
    k=p
    while i<len(leftHalf) and j<len(rightHalf):
        if leftHalf[i]<=rightHalf[j]:
            array[k]=leftHalf[i]
            i+=1
        else:
            array[k]=rightHalf[j]   
            j+=1
        k+=1
    while i<len(leftHalf):
            array[k]=leftHalf[i]
            i+=1
            k+=1
    while j<len(rightHalf):
            array[k]=rightHalf[j]
            j+=1
            k+=1
        
def MergeSort(array,start,end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:  
                data[j], data[j + 1] = data[j + 1], data[j] 

# # Sample scraped data
# scraped_data = [
#     {'title': 'Product A', 'price': 30, 'brand': 'Brand X', 'rating': 4.5, 'discount': 10},
#     {'title': 'Product B', 'price': 20, 'brand': 'Brand Y', 'rating': 4.0, 'discount': 15},
#     {'title': 'Product C', 'price': 25, 'brand': 'Brand Z', 'rating': 5.0, 'discount': 5},
# ]

# # Extract prices for sorting
# prices = [item['discount'] for item in scraped_data]

# # Apply Bubble Sort on the prices
# sorted_prices = MergeSort(prices, 0, len(prices))

# # Update the original scraped data based on sorted prices
# sorted_scraped_data = sorted(scraped_data, key=lambda x: x['discount'])

# # Print the sorted data
# print("Sorted data based on price:")
# for item in sorted_scraped_data:
#     print(item['discount'])


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem

# Sample scraped data
scraped_data = [
    {'title': 'Product A', 'price': 30, 'brand': 'Brand X', 'rating': 4.5, 'discount': 10},
    {'title': 'Product B', 'price': 20, 'brand': 'Brand Y', 'rating': 4.0, 'discount': 15},
    {'title': 'Product C', 'price': 25, 'brand': 'Brand Z', 'rating': 5.0, 'discount': 5},
    {'title': 'Product C', 'price': 25, 'brand': 'Brand Z', 'rating': 5.0, 'discount': 6},
    {'title': 'Product C', 'price': 25, 'brand': 'Brand Z', 'rating': 5.0, 'discount': 8},
    {'title': 'Product C', 'price': 25, 'brand': 'Brand Z', 'rating': 5.0, 'discount': 33},
    {'title': 'Product C', 'price': 25, 'brand': 'Brand Z', 'rating': 5.0, 'discount': 6},
]
original_data = scraped_data.copy()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sortings')
        self.setGeometry(100, 100, 800, 500)

        # Create layout
        layout = QVBoxLayout()

        # Create table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Title', 'Price', 'Brand', 'Rating', 'Discount'])
        self.populate_table(scraped_data)

        # Create button
        self.sort_button1 = QPushButton('Merge Sort')
        self.sort_button1.clicked.connect(self.sort_data)

        self.sort_button = QPushButton('refresh')
        self.sort_button.clicked.connect(self.refresh_data)

        # Add widgets to layout
        layout.addWidget(self.table)
        layout.addWidget(self.sort_button)
        layout.addWidget(self.sort_button1)

        self.setLayout(layout)

    def populate_table(self, data):
        self.table.setRowCount(len(data))
        for row, item in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(item['title']))
            self.table.setItem(row, 1, QTableWidgetItem(str(item['price'])))
            self.table.setItem(row, 2, QTableWidgetItem(item['brand']))
            self.table.setItem(row, 3, QTableWidgetItem(str(item['rating'])))
            self.table.setItem(row, 4, QTableWidgetItem(str(item['discount'])))

    def sort_data(self):
        # Sort the scraped data by discount
        price=[item['price']for item in scraped_data]
        bubble_sort(scraped_data,'discount')

        # Update the table with sorted data
        self.populate_table(scraped_data)
    
    def refresh_data(self):
        # Refresh the scraped data from the website
        self.populate_table(original_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
