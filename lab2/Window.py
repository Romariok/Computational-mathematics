from PyQt5 import QtWidgets
from App import Ui_MainWindow
import Equations
import SystemEquations
import SystemIterations
import Newton
import Iterations
import Chord
import matplotlib.pyplot as plt
import sys


class mywindow(QtWidgets.QMainWindow):
    file_input = False
    system = False
    download = False
    output = ""
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.pltShow)
        self.ui.pushButton.clicked.connect(self.solve)
        self.ui.pushButton_7.clicked.connect(self.solve_system)
        self.ui.pushButton_3.clicked.connect(self.file_toggle)
        self.ui.pushButton_4.clicked.connect(self.download_file)
        self.ui.pushButton_8.clicked.connect(self.file_toggle_system)
        self.ui.tabWidget.currentChanged.connect(self.system_toggle)
        self.file_input = False
        self.download = False

    def system_toggle(self):
        self.system = not self.system
    def download_file(self):
        print("Попытка загрузки")
        if self.download:
            new_file = open("lab2/output.txt", "w+", encoding="utf-8")
            new_file.write(self.output)
            new_file.close()

    def pltShow(self):
        if self.system:
            num = int(self.ui.comboBox_4.currentText())
            if num == 1:
                sys_eq1 = SystemEquations.Equations(num)
                sys_eq2 = SystemEquations.Equations(num + 1)
            else:
                sys_eq1 = SystemEquations.Equations(num + 1)
                sys_eq2 = SystemEquations.Equations(num + 2)
            sys_eq1.draw_graph(-10, 10)
            sys_eq2.draw_graph(-10, 10)
        plt.show()

    def file_toggle(self):
        self.file_input = True
        self.solve()

    def file_toggle_system(self):
        self.file_input = True
        self.solve_system()

    def clear_table(self):
        self.ui.tableWidget.clear()

    def set_table(self, data):
        self.ui.tableWidget.setRowCount(len(data[0]))
        self.ui.tableWidget.setColumnCount(len(data[0][0]))
        for i in range(len(data[0])):
            for j in range(len(data[0][i])):
                self.ui.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(data[0][i][j])
                )
        self.ui.textEdit_4.setText(data[1])

    def solve(self):
        self.download = True
        plt.cla()
        if self.file_input:
            try:
                file = open(self.ui.lineEdit_5.text(), "r")
                a, b, e = map(str, file.readline().replace(",", ".").split())
                try:
                    a = float(a)
                    b = float(b)
                    e = float(e)
                    num = int(self.ui.comboBox.currentText())
                    self.ui.pushButton.setText("Решить")
                    if num < 1 or num > 4:
                        raise ValueError
                except ValueError:
                    self.file_input = False
                    self.ui.pushButton.setText("Введите корректные данные")
                    return
                self.ui.lineEdit.setText(str(a))
                self.ui.lineEdit_2.setText(str(b))
                self.ui.lineEdit_3.setText(str(e))
                self.ui.pushButton.setText("Решить")
            except FileNotFoundError:
                self.file_input = False
                self.ui.pushButton.setText("Введите корректный путь до файла")
                return
            self.file_input = False
        else:
            try:
                a = float(self.ui.lineEdit.text().replace(",", "."))
                b = float(self.ui.lineEdit_2.text().replace(",", "."))
                e = float(self.ui.lineEdit_3.text().replace(",", "."))
                num = int(self.ui.comboBox.currentText())
                self.ui.pushButton.setText("Решить")
            except ValueError:
                self.ui.pushButton.setText("Введите корректные данные")
                return
        if e <= 0 or a >= b:
            self.ui.pushButton.setText("Введите корректные данные")
            return
        self.clear_table()

        eq = Equations.Equation(num)

        num_method = int(self.ui.comboBox_2.currentText())
        if num_method == 1:
            solver = Chord.Chord(eq)
            data = solver.solve(a, b, e)
        elif num_method == 2:
            solver = Newton.Newton(eq)
            data = solver.solve(a, b, e)
        else:
            solver = Iterations.Iteration_Method(eq)
            data = solver.solve(a, b, e)

        if len(data) == 1:
            self.ui.textEdit_4.setText(data[0])
            self.output = data[0]
        else:
            self.output = data[1]
            self.set_table(data)
            k_left, k_right = 1.2, 1.2
            if a > 0:
                k_left = 0.8
            if b < 0:
                k_right = 0.8
            eq.draw_graph(k_left * a, k_right * b)

    def solve_system(self):
        self.download = True
        if self.file_input:
            try:
                file = open(self.ui.lineEdit_14.text(), "r")
                a, b, e = map(str, file.readline().replace(",", ".").split())
                try:
                    a = float(a)
                    b = float(b)
                    e = float(e)
                    num = int(self.ui.comboBox_4.currentText())
                    self.ui.pushButton_7.setText("Решить")
                    if num < 1 or num > 2:
                        raise ValueError
                except ValueError:
                    self.file_input = False
                    self.ui.pushButton_7.setText("Введите корректные данные")
                    return
                self.ui.lineEdit_11.setText(str(a))
                self.ui.lineEdit_12.setText(str(b))
                self.ui.lineEdit_13.setText(str(e))
                self.ui.pushButton_7.setText("Решить")
            except FileNotFoundError:
                self.file_input = False
                self.ui.pushButton_7.setText("Введите корректный путь до файла")
                return
            self.file_input = False
        else:
            try:
                a = float(self.ui.lineEdit_11.text().replace(",", "."))
                b = float(self.ui.lineEdit_12.text().replace(",", "."))
                e = float(self.ui.lineEdit_13.text().replace(",", "."))
                num = int(self.ui.comboBox_4.currentText())
                self.ui.pushButton_7.setText("Решить")
            except ValueError:
                self.ui.pushButton_7.setText("Введите корректные данные")
                return
        if e <= 0:
            self.ui.pushButton_7.setText("Введите корректные данные")
            return
        self.clear_table()
        if num == 1:
            sys_eq1 = SystemEquations.Equations(num)
            sys_eq2 = SystemEquations.Equations(num + 1)
        else:
            sys_eq1 = SystemEquations.Equations(num + 1)
            sys_eq2 = SystemEquations.Equations(num + 2)

        solver = SystemIterations.Iteration_Method(sys_eq1, sys_eq2)
        data = solver.solve(a, b, e)
        if len(data) == 1:
            self.output = data[0]
            self.ui.textEdit_4.setText(data[0])
        else:
            self.output = data[1]
            self.set_table(data)
            x = float(data[0][-1][1])
            sys_eq1.draw_graph(x - 2, x + 2)
            sys_eq2.draw_graph(x - 2, x + 2)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
