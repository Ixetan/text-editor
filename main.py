from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from beck import saveFile, openFile

app = QApplication([])

layout = QVBoxLayout()

buttons_layuot = QHBoxLayout()
open_button = QPushButton("Открыть")
save_button = QPushButton('Сохранить')
buttons_layuot.addWidget(open_button)
buttons_layuot.addWidget(save_button)

editor = QPlainTextEdit()
layout.addLayout(buttons_layuot)
layout.addWidget(editor)

window = QWidget()
window.setLayout(layout)
window.show()

def saveFileButtonHandler():
    file_path = QFileDialog.getSaveFileName()
    saveFile(editor.toPlainText(), file_path[0])

def openFileButtonHandler():
    file_path = QFileDialog.getOpenFileName()
    text = openFile(file_path[0])
    editor.setPlainText(text)
    
save_button.clicked.connect(saveFileButtonHandler)
open_button.clicked.connect(openFileButtonHandler)

app.exec()