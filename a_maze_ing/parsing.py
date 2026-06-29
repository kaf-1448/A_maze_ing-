from configparser import ConfigParser

config = ConfigParser()
config.read("../config.txt")

width = config.getint('WIDTH', 'WIDTH')
print(width)
