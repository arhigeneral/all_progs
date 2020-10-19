import configparser
import os


def createConfig(path):
    """
    Create a config file
    """

    config = configparser.ConfigParser()
    config.add_section("Users")
    config.set("Users","users","1")

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
    path = "Users.ini"
    createConfig(path)
