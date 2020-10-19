from PyQt5 import QtWidgets
import window_design
import sys
import ini


class StarterApp(QtWidgets.QMainWindow, window_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create)


    def create(self):
        ini.createConfig('Форма.ini')
        name = self.comboBox.currentText()
        age = self.comboBox_2.currentText()
        clothes = self.comboBox_3.currentText()
        body_part = self.comboBox_4.currentText()
        body_condition = self.comboBox_5.currentText()
        photo_status = self.comboBox_6.currentText()
        #print('Имя - {}, возраст - {}, одежда - {}, часть тела - {},состояние тела - {},состояние фото - {}'.format(name,age,clothes,body_part,body_condition,photo_status))

        ini.update_setting("Форма.ini","Форма","Имя",name)
        ini.update_setting("Форма.ini","Форма","Проверка возраста",age)
        ini.update_setting("Форма.ini","Форма","Одежда",clothes)
        ini.update_setting("Форма.ini","Форма","Часть тела",body_part)
        ini.update_setting("Форма.ini","Форма","Состояние части тела",body_condition)
        ini.update_setting("Форма.ini","Форма","Состояние фото",photo_status)

        window.close()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = StarterApp()
    window.show()
    app.exec_()
    sys.exit(app.exec_())
