from PyQt5 import QtWidgets
import editor_design
import sys
import configparser
import ini
import main_window

class EditorApp(QtWidgets.QMainWindow, editor_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.close_1)
        self.pushButton.clicked.connect(self.find_user)
        self.pushButton_2.clicked.connect(self.edit_user)
        self.pushButton_4.clicked.connect(self.back)

    def find_user(self):
        config = configparser.ConfigParser()
        config.read("Users.ini")

        user = self.plainTextEdit.toPlainText()

        second_name = config.get("User" + user, "second_name")
        self.plainTextEdit_3.setPlainText(second_name)
        self.plainTextEdit_3.repaint()

        name = config.get("User" + user, "name")
        self.plainTextEdit_2.setPlainText(name)
        self.plainTextEdit_2.repaint()

        sex = config.get("User" + user, "sex")
        self.plainTextEdit_6.setPlainText(sex)
        self.plainTextEdit_6.repaint()

        birthday = config.get("User" + user, "birthday")
        self.plainTextEdit_4.setPlainText(birthday)
        self.plainTextEdit_4.repaint()

        adres = config.get("User" + user, "adres")
        self.plainTextEdit_5.setPlainText(adres)
        self.plainTextEdit_5.repaint()

        job = config.get("User" + user, "job")
        self.plainTextEdit_7.setPlainText(job)
        self.plainTextEdit_7.repaint()

        main_adres = config.get("User" + user, "main_adres")
        self.plainTextEdit_8.setPlainText(main_adres)
        self.plainTextEdit_8.repaint()

    def edit_user(self):

        user = self.plainTextEdit.toPlainText()

        second_name = self.plainTextEdit_3.toPlainText()
        print(second_name)
        name = self.plainTextEdit_2.toPlainText()
        print(name)
        sex = self.plainTextEdit_6.toPlainText()
        print(sex)
        birthday = self.plainTextEdit_4.toPlainText()
        print(birthday)
        adres = self.plainTextEdit_5.toPlainText()
        print(adres)
        job = self.plainTextEdit_7.toPlainText()
        print(job)
        main_adres = self.plainTextEdit_8.toPlainText()
        print(main_adres)

        ini.update_setting("Users.ini","User" + user, "second_name",second_name)
        ini.update_setting("Users.ini","User" + user, "name",name)
        ini.update_setting("Users.ini","User" + user, "sex",sex)
        ini.update_setting("Users.ini","User" + user, "birthday",birthday)
        ini.update_setting("Users.ini","User" + user, "adres",adres)
        ini.update_setting("Users.ini","User" + user, "job",job)
        ini.update_setting("Users.ini","User" + user, "main_adres",main_adres)

        self.plainTextEdit.setPlainText('')
        self.plainTextEdit.repaint()

        self.plainTextEdit_2.setPlainText('')
        self.plainTextEdit_2.repaint()

        self.plainTextEdit_3.setPlainText('')
        self.plainTextEdit_3.repaint()

        self.plainTextEdit_4.setPlainText('')
        self.plainTextEdit_4.repaint()

        self.plainTextEdit_5.setPlainText('')
        self.plainTextEdit_5.repaint()

        self.plainTextEdit_6.setPlainText('')
        self.plainTextEdit_6.repaint()

        self.plainTextEdit_7.setPlainText('')
        self.plainTextEdit_7.repaint()

        self.plainTextEdit_8.setPlainText('')
        self.plainTextEdit_8.repaint()

    def close_1(self):

        if __name__ == '__main__':
            window.close()
            sys.exit(app.exec_())
        else:
            self.window.close()

    def back(self):

        config = configparser.ConfigParser()
        config.read("RunTime.ini")
        Exec = config.get("Run_Time","Exec")


        main_window.MainLabApp.window_2 = main_window.MainLabApp()
        main_window.MainLabApp.window_2.show()
        if Exec == "1":
            main_window.MainLabApp.app_2 = QtWidgets.QApplication([])
            main_window.MainLabApp.app_2.exec_()
            ini.update_setting("RunTime.ini","Run_Time","Exec","2")

        self.window.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = EditorApp()
    #использовать многопоточность чтобы не знаходить сюда каждый раз
    window.show()
    app.exec_()
