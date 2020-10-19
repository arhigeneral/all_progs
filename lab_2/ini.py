import configparser
import os


def createConfig(path):
    """
    Create a config file
    """

    config = configparser.ConfigParser()
    config.add_section("Default")
    config.set("Default", "second_name", "Popov")
    config.set("Default", "name", "Saveli")
    config.set("Default", "sex", "male")
    config.set("Default", "birthday", "18:09:1999")
    config.set("Default", "adres", "ne skajy))")
    config.set("Default", "job", "student")
    config.set("Default", "main_adres", "toje ne skajy))")
    config.add_section("Deleted")
    config.set("Deleted", "second_name", "")
    config.set("Deleted", "name", "")
    config.set("Deleted", "sex", "")
    config.set("Deleted", "birthday", "")
    config.set("Deleted", "adres", "")
    config.set("Deleted", "job", "")
    config.set("Deleted", "main_adres", "")
    config.add_section("Closed")
    config.set("Closed", "second_name", "")
    config.set("Closed", "name", "")
    config.set("Closed", "sex", "")
    config.set("Closed", "birthday", "")
    config.set("Closed", "adres", "")
    config.set("Closed", "job", "")
    config.set("Closed", "main_adres", "")
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
    path = "settings.ini"
    createConfig(path)
