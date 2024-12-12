import sys
import nltk
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QFileDialog)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Install NLTK resources (only run once)
nltk.download('punkt_tab')
# nltk.download('stopwords')

# Preprocess the text by tokenizing, removing punctuation and stopwords
def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Lowercasing to make comparison case-insensitive
    tokens = [word for word in tokens if word.isalpha()]  # Remove punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
    return " ".join(tokens)

# Function to compute Cosine Similarity
def cosine_sim(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity_matrix[0][0]

# Function to compute Jaccard Similarity
def jaccard_sim(text1, text2):
    set1 = set(text1.split())
    set2 = set(text2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

# Function to read text from different file formats
def read_file(file_path):
    if not os.path.exists(file_path):
        return None
    try:
        ext = file_path.split('.')[-1].lower()
        if ext in ['txt', 'py', 'cpp']:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        elif ext == 'docx':
            import docx
            doc = docx.Document(file_path)
            text = []
            for para in doc.paragraphs:
                text.append(para.text)
            return '\n'.join(text)
        else:
            return "Unsupported file type"
    except Exception as e:
        return f"Error reading file: {str(e)}"

# Function to detect plagiarism
def detect_plagiarism(doc1, doc2, threshold=0.7):
    doc1 = preprocess_text(doc1)
    doc2 = preprocess_text(doc2)

    # Compute Cosine Similarity
    cos_sim = cosine_sim(doc1, doc2)
    # Compute Jaccard Similarity
    jac_sim = jaccard_sim(doc1, doc2)

    result_text = f"<b>Cosine Similarity:</b> {cos_sim:.4f}<br><b>Jaccard Similarity:</b> {jac_sim:.4f}<br>"

    # Check if plagiarism is detected
    if cos_sim > threshold or jac_sim > threshold:
        result_text += "<b style='color:red;'>Plagiarism detected!</b>"
    else:
        result_text += "<b style='color:green;'>No plagiarism detected.</b>"

    return result_text

# PyQt5 GUI for plagiarism detection system
class PlagiarismCheckerGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize UI components
        self.init_ui()

    def init_ui(self):
        # Set window title and size
        self.setWindowTitle('Plagiarism Detection System')
        self.setGeometry(100, 100, 700, 500)

        # Main layout
        main_layout = QVBoxLayout()

        # Title label
        title_label = QLabel('Plagiarism Detection System')
        title_label.setFont(QFont('Arial', 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # File input layout
        file_layout = QHBoxLayout()

        self.file1_path = QLineEdit(self)
        self.file1_path.setPlaceholderText('Select the first file')
        file_layout.addWidget(self.file1_path)

        self.file2_path = QLineEdit(self)
        self.file2_path.setPlaceholderText('Select the second file')
        file_layout.addWidget(self.file2_path)

        main_layout.addLayout(file_layout)

        # Buttons layout
        buttons_layout = QHBoxLayout()

        self.select_file1_btn = QPushButton('Browse File 1', self)
        self.select_file2_btn = QPushButton('Browse File 2', self)
        self.check_plagiarism_btn = QPushButton('Check Plagiarism', self)
        buttons_layout.addWidget(self.select_file1_btn)
        buttons_layout.addWidget(self.select_file2_btn)
        buttons_layout.addWidget(self.check_plagiarism_btn)

        main_layout.addLayout(buttons_layout)

        # Result area
        self.result_label = QLabel('Result:')
        self.result_label.setFont(QFont('Arial', 14))
        main_layout.addWidget(self.result_label)

        self.result_area = QTextEdit(self)
        self.result_area.setFont(QFont('Courier New', 12))
        self.result_area.setReadOnly(True)
        main_layout.addWidget(self.result_area)

        # Set layout to the window
        self.setLayout(main_layout)

        # Connect buttons to actions
        self.select_file1_btn.clicked.connect(self.select_file1)
        self.select_file2_btn.clicked.connect(self.select_file2)
        self.check_plagiarism_btn.clicked.connect(self.check_plagiarism)

    # Function to open file dialog for the first file
    def select_file1(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select File 1', '', 'All Files (*.*);;Text Files (*.txt);;Python Files (*.py);;C++ Files (*.cpp);;Word Files (*.docx)')
        if file_path:
            self.file1_path.setText(file_path)

    # Function to open file dialog for the second file
    def select_file2(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select File 2', '', 'All Files (*.*);;Text Files (*.txt);;Python Files (*.py);;C++ Files (*.cpp);;Word Files (*.docx)')
        if file_path:
            self.file2_path.setText(file_path)

    # Function to check plagiarism
    def check_plagiarism(self):
        file1 = self.file1_path.text()
        file2 = self.file2_path.text()

        if not file1 or not file2:
            self.result_area.setHtml('<b style="color:red;">Please select two files to compare.</b>')
            return

        # Read the files
        doc1 = read_file(file1)
        doc2 = read_file(file2)

        if not doc1 or not doc2:
            self.result_area.setHtml('<b style="color:red;">Error reading one or both files.</b>')
            return

        # Perform plagiarism check
        result = detect_plagiarism(doc1, doc2)
        self.result_area.setHtml(result)

# Run the PyQt5 application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlagiarismCheckerGUI()
    window.show()
    sys.exit(app.exec_())