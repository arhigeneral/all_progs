import configparser
import os


def createConfig(path):
    """
    Create a config file
    """

    config = configparser.ConfigParser()
    config.add_section("Форма")
    config.set("Форма", "Имя", "")
    config.set("Форма", "Проверка возраста", "")
    config.set("Форма", "Одежда", "")
    config.set("Форма", "Часть тела", "")
    config.set("Форма", "Состояние части тела", "")
    config.set("Форма", "Состояние фото", "")

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

def update_setting(path, section, setting, value):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "Форма.ini"
    createConfig(path)
