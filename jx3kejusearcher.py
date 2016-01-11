# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
import PyQt4
from PyQt4 import QtGui
from Ui_jx3kejusearcher import Ui_MainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow

# import customer module
import PyJX3KeJu

# define title name
TITLE_NAME = '剑网3科举查询器 --- 电五唯满侠-东村西篱帮会福利版'
WELCOME_TXT = u'''\
使用说明：
---------------------------------------------------------------
在上面的那个框框输入所要查询的科举考试题目首字母，标点符号等忽略。
按 ESC    自动清除所有查询结果。
按 Alt+Q 退出程序。

中恶亲友小菜帮《东村西篱》来各种休闲党，成就党，PVX，PVP和PVG！！
15分钟神行和骑马跑商已开，菜地随便种！
帮会YY 71075621


一入此谷，永不受苦！


一入唐门，当捍卫唐门声誉，与同门互为兄弟，绝不仗技害人!



版本历史：
1.  2015-12-13    v0.1.0          第一次发布
2.  2016-01-03    v0.1.1          增加图标
'''


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("MainWindow", TITLE_NAME, None, QtGui.QApplication.UnicodeUTF8))
        self.input_line.setText(u'请输入题目的首字母...')
        self.ans_txt.setText(WELCOME_TXT)

    @pyqtSignature("QString")
    def on_input_line_textChanged(self, p0):
        self.search_question()
    
    @pyqtSignature("")
    def on_input_line_returnPressed(self):
        self.search_question()

    @pyqtSignature("")
    def on_action_ESC_triggered(self):
        self.input_line.clear()
        self.ans_txt.clear()

    def search_question(self):
        answers = PyJX3KeJu.SearchMain(self.input_line.text())
        self.ans_txt.setText(answers)


if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
    

