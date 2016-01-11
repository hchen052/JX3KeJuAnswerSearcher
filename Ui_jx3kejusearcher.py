# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PythonCodeLib\JX3KeJuAnswerSearcher\jx3kejusearcher.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(547, 826)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/icons/Search96.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.input_line = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(9)
        self.input_line.setFont(font)
        self.input_line.setObjectName(_fromUtf8("input_line"))
        self.verticalLayout.addWidget(self.input_line)
        self.ans_txt = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.ans_txt.setFont(font)
        self.ans_txt.setObjectName(_fromUtf8("ans_txt"))
        self.verticalLayout.addWidget(self.ans_txt)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 547, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menuBar)
        self.action_ESC = QtGui.QAction(MainWindow)
        self.action_ESC.setSoftKeyRole(QtGui.QAction.NoSoftKey)
        self.action_ESC.setObjectName(_fromUtf8("action_ESC"))
        self.action_Alt_Q = QtGui.QAction(MainWindow)
        self.action_Alt_Q.setObjectName(_fromUtf8("action_Alt_Q"))
        self.menu.addAction(self.action_ESC)
        self.menu.addSeparator()
        self.menu.addAction(self.action_Alt_Q)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Alt_Q, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.input_line, QtCore.SIGNAL(_fromUtf8("selectionChanged()")), self.input_line.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.input_line.setText(_translate("MainWindow", "请输入题目的首字母:(不一定需要从头开始)", None))
        self.menu.setTitle(_translate("MainWindow", "点我点我....", None))
        self.action_ESC.setText(_translate("MainWindow", "清空", None))
        self.action_ESC.setShortcut(_translate("MainWindow", "Esc", None))
        self.action_Alt_Q.setText(_translate("MainWindow", "退出", None))
        self.action_Alt_Q.setShortcut(_translate("MainWindow", "Alt+Q", None))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

