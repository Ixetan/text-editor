from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QColor
from beck import saveFile, openFile, parseText

colors = {
    'keyword': QColor(255, 0, 255),
    'black': QColor(0, 0, 0)
}

app = QApplication([])

layout = QVBoxLayout()

buttons_layuot = QHBoxLayout()
open_button = QPushButton("Заопенить")
save_button = QPushButton('Сохранить')
buttons_layuot.addWidget(open_button)
buttons_layuot.addWidget(save_button)

editor = QTextEdit()
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
    text = parseText(openFile(file_path[0]))
    
    for line in text:
        for word in line:
            editor.setTextColor(colors[word['color']])
            editor.insertPlainText(f'{word["text"]} ')
        editor.insertPlainText('\n')
    
    editor.setTextColor(colors['black'])
    

save_button.clicked.connect(saveFileButtonHandler)
open_button.clicked.connect(openFileButtonHandler)

app.exec()