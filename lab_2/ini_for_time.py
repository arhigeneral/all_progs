import configparser
import os


def createConfig(path):
    """
    Create a config file
    """

    config = configparser.ConfigParser()
    config.add_section("Run_Time")
    config.set("Run_Time", "MainWindow", "315 720")
    config.set("Run_Time", "label", "70 20 61 41")
    config.set("Run_Time", "label_2", "150 70 121 31")
    config.set("Run_Time", "label_3", "150 120 121 31")
    config.set("Run_Time", "label_4", "150 180 121 31")
    config.set("Run_Time", "label_5", "150 230 121 31")
    config.set("Run_Time", "label_6", "150 280 121 31")
    config.set("Run_Time", "pushButton", "20 440 81 23")
    config.set("Run_Time", "pushButton_2", "110 440 81 23")
    config.set("Run_Time", "pushButton_3", "200 440 81 23")
    config.set("Run_Time", "pushButton_4", "110 470 81 23")
    config.set("Run_Time", "pushButton_5", "20 470 81 23")
    config.set("Run_Time", "pushButton_6", "200 470 81 23")
    config.set("Run_Time", "pushButton_7", "110 500 81 23")
    config.set("Run_Time", "plainTextEdit", "20 70 104 31")
    config.set("Run_Time", "plainTextEdit_2", "20 120 104 31")
    config.set("Run_Time", "plainTextEdit_3", "20 180 104 31")
    config.set("Run_Time", "plainTextEdit_4", "20 240 104 31")
    config.set("Run_Time", "plainTextEdit_5", "20 290 104 31")
    config.set("Run_Time", "plainTextEdit_6", "20 340 104 31")
    config.set("Run_Time", "plainTextEdit_7", "20 390 104 31")
    config.set("Run_Time","OurTime","")
    config.set("Run_Time","Exec","0")

    with open(path, "w") as config_file:
        config.write(config_file)

def get_config(path):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


if __name__ == "__main__":
    path = "RunTime.ini"
    createConfig(path)
