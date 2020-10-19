from PyQt5 import QtWidgets
import design
import configparser
import ini
import design_start
import sys
import ini_for_time
import editor_window
import all_users_window


class MainLabApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.cleare)
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton_3.clicked.connect(self.restore)
        self.pushButton_4.clicked.connect(self.close_1)
        self.pushButton_5.clicked.connect(self.edit)
        self.pushButton_6.clicked.connect(self.show_all)
        self.pushButton_7.clicked.connect(self.add)


    def cleare(self):
        second_name = self.plainTextEdit.toPlainText()
        name = self.plainTextEdit_2.toPlainText()
        sex = self.plainTextEdit_3.toPlainText()
        birthday = self.plainTextEdit_4.toPlainText()
        adres = self.plainTextEdit_5.toPlainText()
        job = self.plainTextEdit_6.toPlainText()
        main_adres = self.plainTextEdit_7.toPlainText()


        ini.update_setting("settings.ini","Deleted","second_name",second_name)
        ini.update_setting("settings.ini","Deleted","name",name)
        ini.update_setting("settings.ini","Deleted","sex",sex)
        ini.update_setting("settings.ini","Deleted","birthday",birthday)
        ini.update_setting("settings.ini","Deleted","adres",adres)
        ini.update_setting("settings.ini","Deleted","job",job)
        ini.update_setting("settings.ini","Deleted","main_adres",main_adres)


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


    def restore(self):

        config = configparser.ConfigParser()
        config.read("settings.ini")

        second_name = config.get("Deleted", "second_name")
        self.plainTextEdit.setPlainText(second_name)
        self.plainTextEdit.repaint()

        name = config.get("Deleted", "name")
        self.plainTextEdit_2.setPlainText(name)
        self.plainTextEdit_2.repaint()

        sex = config.get("Deleted", "sex")
        self.plainTextEdit_3.setPlainText(sex)
        self.plainTextEdit_3.repaint()

        birthday = config.get("Deleted", "birthday")
        self.plainTextEdit_4.setPlainText(birthday)
        self.plainTextEdit_4.repaint()

        adres = config.get("Deleted", "adres")
        self.plainTextEdit_5.setPlainText(adres)
        self.plainTextEdit_5.repaint()

        job = config.get("Deleted", "job")
        self.plainTextEdit_6.setPlainText(job)
        self.plainTextEdit_6.repaint()

        main_adres = config.get("Deleted", "main_adres")
        self.plainTextEdit_7.setPlainText(main_adres)
        self.plainTextEdit_7.repaint()

    def cancel(self):

        config = configparser.ConfigParser()
        config.read("settings.ini")

        second_name = config.get("Default", "second_name")
        self.plainTextEdit.setPlainText(second_name)
        self.plainTextEdit.repaint()

        name = config.get("Default", "name")
        self.plainTextEdit_2.setPlainText(name)
        self.plainTextEdit_2.repaint()

        sex = config.get("Default", "sex")
        self.plainTextEdit_3.setPlainText(sex)
        self.plainTextEdit_3.repaint()

        birthday = config.get("Default", "birthday")
        self.plainTextEdit_4.setPlainText(birthday)
        self.plainTextEdit_4.repaint()

        adres = config.get("Default", "adres")
        self.plainTextEdit_5.setPlainText(adres)
        self.plainTextEdit_5.repaint()

        job = config.get("Default", "job")
        self.plainTextEdit_6.setPlainText(job)
        self.plainTextEdit_6.repaint()

        main_adres = config.get("Default", "main_adres")
        self.plainTextEdit_7.setPlainText(main_adres)
        self.plainTextEdit_7.repaint()

    def close_1(self):

        second_name = self.plainTextEdit.toPlainText()
        name = self.plainTextEdit_2.toPlainText()
        sex = self.plainTextEdit_3.toPlainText()
        birthday = self.plainTextEdit_4.toPlainText()
        adres = self.plainTextEdit_5.toPlainText()
        job = self.plainTextEdit_6.toPlainText()
        main_adres = self.plainTextEdit_7.toPlainText()

        ini.update_setting("settings.ini","Closed","second_name",second_name)
        ini.update_setting("settings.ini","Closed","name",name)
        ini.update_setting("settings.ini","Closed","sex",sex)
        ini.update_setting("settings.ini","Closed","birthday",birthday)
        ini.update_setting("settings.ini","Closed","adres",adres)
        ini.update_setting("settings.ini","Closed","job",job)
        ini.update_setting("settings.ini","Closed","main_adres",main_adres)


        self.window_2.close()
        sys.exit(self.app_2.exec_())


    def add(self):

        config = configparser.ConfigParser()
        config.read("Users.ini")
        i = config.get("Users","users")

        config.add_section("User" + i)
        print(i)

        with open("Users.ini", "w") as config_file:
            config.write(config_file)


        second_name = self.plainTextEdit.toPlainText()
        name = self.plainTextEdit_2.toPlainText()
        sex = self.plainTextEdit_3.toPlainText()
        birthday = self.plainTextEdit_4.toPlainText()
        adres = self.plainTextEdit_5.toPlainText()
        job = self.plainTextEdit_6.toPlainText()
        main_adres = self.plainTextEdit_7.toPlainText()

        ini.update_setting("Users.ini","User" + i,"second_name",second_name)
        ini.update_setting("Users.ini","User" + i,"name",name)
        ini.update_setting("Users.ini","User" + i,"sex",sex)
        ini.update_setting("Users.ini","User" + i,"birthday",birthday)
        ini.update_setting("Users.ini","User" + i,"adres",adres)
        ini.update_setting("Users.ini","User" + i,"job",job)
        ini.update_setting("Users.ini","User" + i,"main_adres",main_adres)

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

        ini.update_setting("Users.ini","Users","users",str(int(i) + 1))

    def edit(self):

        config = configparser.ConfigParser()
        config.read("RunTime.ini")
        Exec = config.get("Run_Time","Exec")

        editor_window.EditorApp.window = editor_window.EditorApp()
        editor_window.EditorApp.window.show()
        if Exec == "0":
            editor_window.EditorApp.app = QtWidgets.QApplication([])
            editor_window.EditorApp.app.exec_()
            ini.update_setting("RunTime.ini","Run_Time","Exec","1")


    def show_all(self):

        all_users_window.AllUsersApp.window = all_users_window.AllUsersApp()
        all_users_window.AllUsersApp.window.show()


class StarterApp(QtWidgets.QMainWindow, design_start.Ui_MainWindow,design.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        config = configparser.ConfigParser()
        config.read("RunTime.ini")
        self.pushButton.clicked.connect(self.RunTime)
        self.pushButton_2.clicked.connect(self.DesignTime)


    def RunTime(self):

        ini.update_setting("RunTime.ini","Run_Time","ourtime","0")
        MainLabApp.app_2 = QtWidgets.QApplication([])
        MainLabApp.window_2 = MainLabApp()
        MainLabApp.window_2.show()
        window.close()


    def DesignTime(self):

        ini.update_setting("RunTime.ini","Run_Time","ourtime","1")
        MainLabApp.app_2 = QtWidgets.QApplication([])
        MainLabApp.window_2 = MainLabApp()
        MainLabApp.window_2.show()
        window.close()


if __name__ == '__main__':
    ini.update_setting("RunTime.ini","Run_Time","ourtime"," ")
    ini.update_setting("RunTime.ini","Run_Time","Exec","0")
    app = QtWidgets.QApplication([])
    window = StarterApp()
    #использовать многопоточность чтобы не знаходить сюда каждый раз
    window.show()
    app.exec_()
    sys.exit(app.exec_())
