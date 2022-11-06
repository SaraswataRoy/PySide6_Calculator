# importing libraries
# from typing_extensions import Self
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtCore import *

import sys
from pathlib import Path

class Window(QMainWindow):

	def __init__(self, holder):
		super().__init__()

		# setting title
		self.setWindowTitle("Calculator")

		# setting geometry
		self.setGeometry(100, 100, 360, 350)

		# calling method
		self.UiComponents(holder)

		# method for widgets
	def UiComponents(self, holder):

		widgets = QVBoxLayout(holder)

		self.label = QLabel(self)

		# creating label multi line
		self.label.setWordWrap(True)
        
		# setting alignment to the label
		self.label.setAlignment(Qt.AlignRight)
        
		del_clear = QHBoxLayout(holder)

		widgets.addWidget(self.label)

        # clear button
		push_clear = QPushButton("Clear", self)
		push_clear.setProperty('cssClass', 'push_clear')

		# del one character button
		push_del = QPushButton("Del", self)
		push_del.setProperty('cssClass', 'push_del')

		del_clear.addWidget(push_clear)
		del_clear.addSpacing(1)
		del_clear.addWidget(push_del)
		widgets.addLayout(del_clear)

		first_row = QHBoxLayout(holder)

		# creating a push button
		push1 = QPushButton("1", self)
		push2 = QPushButton("2", self)
		push3 = QPushButton("3", self)
		push_mul = QPushButton("*", self)

		first_row.addWidget(push1)
		first_row.addWidget(push2)
		first_row.addWidget(push3)
		first_row.addWidget(push_mul)
		widgets.addLayout(first_row)


		second_row = QHBoxLayout(holder)
		# creating a push button
		push4 = QPushButton("4", self)
		# creating a push button
		push5 = QPushButton("5", self)
		# creating a push button
		push6 = QPushButton("6", self)
		push_minus = QPushButton("-", self)

		second_row.addWidget(push4)
		second_row.addWidget(push5)
		second_row.addWidget(push6)
		second_row.addWidget(push_minus)
		widgets.addLayout(second_row)

		third_row = QHBoxLayout(holder)
		# creating a push button
		push7 = QPushButton("7", self)
		# creating a push button
		push8 = QPushButton("8", self)
		# creating a push button
		push9 = QPushButton("9", self)
        # creating a push button
		push_plus = QPushButton("+", self)

		third_row.addWidget(push7)
		third_row.addWidget(push8)
		third_row.addWidget(push9)
		third_row.addWidget(push_plus)
		widgets.addLayout(third_row)

		fourth_row = QHBoxLayout(holder)
		# creating a push button
		push0 = QPushButton("0", self)
		# creating a push button
		push_point = QPushButton(".", self)
		# creating a push button
		push_div = QPushButton("/", self)
        # creating a push button
		push_equal = QPushButton("=", self)

		fourth_row.addWidget(push0)
		fourth_row.addWidget(push_point)
		fourth_row.addWidget(push_div)
		fourth_row.addWidget(push_equal)
		k_effect = QGraphicsColorizeEffect()
		k_effect.setColor(Qt.blue)
		push_equal.setGraphicsEffect(k_effect)
		widgets.addLayout(fourth_row)

		# adding action to each of the button
		push_minus.clicked.connect(self.action_minus)
		push_equal.clicked.connect(self.action_equal)
		push0.clicked.connect(self.action0)
		push1.clicked.connect(self.action1)
		push2.clicked.connect(self.action2)
		push3.clicked.connect(self.action3)
		push4.clicked.connect(self.action4)
		push5.clicked.connect(self.action5)
		push6.clicked.connect(self.action6)
		push7.clicked.connect(self.action7)
		push8.clicked.connect(self.action8)
		push9.clicked.connect(self.action9)
		push_div.clicked.connect(self.action_div)
		push_mul.clicked.connect(self.action_mul)
		push_plus.clicked.connect(self.action_plus)
		push_point.clicked.connect(self.action_point)
		push_clear.clicked.connect(self.action_clear)
		push_del.clicked.connect(self.action_del)

		holder.setLayout(widgets)
		holder.show() 

	def action_equal(self):

		# get the label text
		equation = self.label.text()

		try:
			# getting the ans
			ans = eval(equation)

			# setting text to the label
			self.label.setText(str(ans))

		except:
			# setting text to the label
			self.label.setText("Wrong Input")

	def action_plus(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + " + ")

	def action_minus(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + " - ")

	def action_div(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + " / ")

	def action_mul(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + " * ")

	def action_point(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + ".")

	def action0(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "0")

	def action1(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "1")

	def action2(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "2")

	def action3(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "3")

	def action4(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "4")

	def action5(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "5")

	def action6(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "6")

	def action7(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "7")

	def action8(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "8")

	def action9(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "9")

	def action_clear(self):
		# clearing the label text
		self.label.setText("")

	def action_del(self):
		# clearing a single digit
		text = self.label.text()
		print(text[:len(text)-1])
		self.label.setText(text[:len(text)-1])

if __name__ == '__main__':
    try:
        # create PySide6 app
        App = QApplication(sys.argv)
        holder = QWidget()
        window = Window(holder)
        # window.show()
        if Path('style.qss').exists():
            with open('style.qss', 'r', encoding ='utf-8') as cssf:
                _app_style = cssf.read()
                App.setStyleSheet(_app_style)
        # start the app
        sys.exit(App.exec())
    except Exception as e:
        print(f'System Error-Calculator failed: {e}')
