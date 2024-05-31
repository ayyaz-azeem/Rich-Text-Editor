from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import * # word to pdf converter
from PyQt5.QtCore import *
#from PyQt5.Qt import *
import sys

class RTE(QMainWindow):
    def __init__(self):
        super(RTE,self).__init__()
        
        # editor
        self.editor = QTextEdit()
        self.fontSizeBox = QSpinBox()
        default_font_size = 24

        font = QFont('Times',default_font_size)
        self.editor.setFont(font)
        self.path = ""

        self.setCentralWidget(self.editor)

        # set window title
        self.setWindowTitle('Rich Text Editor by Ayyaz Azeem')
        
        #full sized window
        self.showMaximized()
        
        # adding toolbar using this command
        self.create_tool_bar()
        self.editor.setFontPointSize(default_font_size)

    # tool bar at the top (undo redo etc functions)
    def create_tool_bar(self):
        toolbar = QToolBar()

        # 0 save Button
        save_action = QAction(QIcon('icons/0save2.png'),'save',self)
        save_action.triggered.connect(self.saveFile)
        toolbar.addAction(save_action)

        toolbar.addSeparator()

        # 1 undo Button
        undoBtn = QAction(QIcon('icons/1undo.png'),'undo',self)
        undoBtn.triggered.connect(self.editor.undo)
        toolbar.addAction(undoBtn)

        # 2 redo Button
        redoBtn = QAction(QIcon('icons/2redo.png'),'redo',self)
        redoBtn.triggered.connect(self.editor.redo)
        toolbar.addAction(redoBtn)

        toolbar.addSeparator()

        # 3 copy Button
        copyBtn = QAction(QIcon('icons/3copy.png'),'copy',self)
        copyBtn.triggered.connect(self.editor.copy)
        toolbar.addAction(copyBtn)

        # 4 cut Button
        cutBtn = QAction(QIcon('icons/4cut.png'),'cut',self)
        cutBtn.triggered.connect(self.editor.cut)
        toolbar.addAction(cutBtn)

        # 5 paste Button
        pasteBtn = QAction(QIcon('icons/5paste4.png'),'paste',self)
        pasteBtn.triggered.connect(self.editor.paste)
        toolbar.addAction(pasteBtn)

        toolbar.addSeparator()
        
        self.fontBox=QComboBox(self)
        self.fontBox.addItems(
            ["Courier Std",
            "Hellentic Typrwriter Regular",
            "Arial",
            "SansSerif",
            "Helvetica",
            "Times",
            "Monospace"])
        self.fontBox.activated.connect(self.setFont)
        toolbar.addWidget(self.fontBox)

        self.fontSizeBox.setValue(24)
        self.fontSizeBox.valueChanged.connect(self.setFontSize)
        toolbar.addWidget(self.fontSizeBox)

        toolbar.addSeparator()

        # 6 leftAllign Button
        leftAllign = QAction(QIcon('icons/6left-align2.png'),'Left Allign',self)
        leftAllign.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignLeft))
        toolbar.addAction(leftAllign)

        # 7 centerAllign Button
        centerAllign = QAction(QIcon('icons/7center-align2.png'),'Center Allign',self)
        centerAllign.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignCenter))
        toolbar.addAction(centerAllign)

        # 8 rightAllign Button
        rightAllign = QAction(QIcon('icons/8right-align2.png'),'Right Allign',self)
        rightAllign.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignRight))
        toolbar.addAction(rightAllign)

        toolbar.addSeparator()

        # 9 Bold Button
        boldBtn = QAction(QIcon('icons/9bold.png'),'Bold',self)
        boldBtn.triggered.connect(self.boldText9)
        toolbar.addAction(boldBtn)

        # 10 underline Button
        underlineBtn = QAction(QIcon('icons/10underline.png'),'Underline',self)
        underlineBtn.triggered.connect(self.underlineText10)
        toolbar.addAction(underlineBtn)

        # 11 italic Button
        italicBtn = QAction(QIcon('icons/11italic.png'),'italic',self)
        italicBtn.triggered.connect(self.italicText11)
        toolbar.addAction(italicBtn)

        self.addToolBar(toolbar) # show toolbar
    
    def setFontSize(self):
        value = self.fontSizeBox.value()
        self.editor.setFontPointSize(value)
    
    def setFont(self):
        font = self.fontBox.currentText()
        self.editor.setCurrentFont(QFont(font))
    
    def italicText11(self):
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not(state))
    
    def underlineText10(self):
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not(state))
    
    def boldText9(self):
        if self.editor.fontWeight != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)
    
    def saveFile(self):
        print(self.path)
        if self.path =='':
            self.file_saveas()
        text = self.editor.toPlainText()
        try:
            with open(self.path,'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)
    
    def file_saveas(self):
        self.path, _ = QFileDialog.getSaveFileName(
            self,
            "Save file",
            "", 
            "text documents (*.text);Text documents (*.txt);All files(*.*)"
            )
        if self.path == '':
            return
        text = self.editor.toPlainText()
        try:
            with open(path,'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

app=QApplication(sys.argv)
window=RTE()
window.show()
sys.exit(app.exec_())