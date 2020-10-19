from PyQt5 import QtWidgets
import all_users_design
import configparser



class AllUsersApp(QtWidgets.QMainWindow, all_users_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        config = configparser.ConfigParser()
        config.read("Users.ini")
        for i in range(1,int(config.get("Users","users"))):
            second_name = config.get("User" + str(i), "second_name")
            text = second_name + ' '

            name = config.get("User" + str(i), "name")
            text += name + ' '

            sex = config.get("User" + str(i), "sex")
            text += sex + ' '

            birthday = config.get("User" + str(i), "birthday")
            text += birthday + ' '

            adres = config.get("User" + str(i), "adres")
            text += adres + ' '

            job = config.get("User" + str(i), "job")
            text += job + ' '

            main_adres = config.get("User" + str(i), "main_adres")
            text += main_adres

            self.textBrowser.append(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = AllUsersApp()
    window.show()
    app.exec_()
