from PyQt5 import QtWidgets
import firs_window_design
import list_design
import perekrestok
import time
import threading

class MainWindowApp(QtWidgets.QMainWindow, firs_window_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button)



    def button(self):

        global cars_amount
        cars_amount = int(self.plainTextEdit.toPlainText())
        ListApp.app = QtWidgets.QApplication([])
        ListApp.window_1 = ListApp()
        #использовать многопоточность чтобы не знаходить сюда каждый раз
        ListApp.window_1.show()
        window.close()





class ListApp(QtWidgets.QMainWindow, list_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        up_to_down, down_to_up, left_to_right, right_to_left = perekrestok.wat_lists(cars_amount)
        self.textBrowser.append("Количество машин")
        self.textBrowser.append(str(cars_amount))
        self.textBrowser.append("Север - Юг")
        self.textBrowser.append(str(up_to_down))
        self.textBrowser.append("Юг - Север")
        self.textBrowser.append(str(down_to_up))
        self.textBrowser.append("Запад - Восток")
        self.textBrowser.append(str(left_to_right))
        self.textBrowser.append("Восток - Запад")
        self.textBrowser.append(str(right_to_left))
        global main_list
        main_list = perekrestok.perekrestok(up_to_down,down_to_up,left_to_right,right_to_left)
        thread = threading.Thread(target=self.receive)
        thread.start()

    def receive(self):
        for i in range(0,len(main_list)):
            if i != 0:
               time.sleep(main_list[i][1] - main_list[i-1][1])
            else:
                time.sleep(main_list[i][1])
            self.textBrowser.append(str(main_list[i]))








if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindowApp()
    #использовать многопоточность чтобы не знаходить сюда каждый раз
    window.show()
    app.exec_()
